def main():
    import sys
    input = lambda:sys.stdin.readline().strip()
    
    N,Q = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N-1)]
    PX = [list(map(int,input().split())) for _ in range(Q)]

    # queryを一個づつ処理すると間に合わない。
    # pxをまとめ上げ、かつ隣接nodeに逐次加算していけばよい
    from collections import deque

    tree = [[] for i in range(N)]
    for a,b in AB:
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    
    score = [0]*N
    for p,x in PX:
        score[p-1]+=x

    queue = deque([0])
    visited = [False]*N
    visited[0] = True

    while queue:
        x = queue.pop()

        for i in tree[x]:
            if not visited[i]:
                queue.append(i)
                score[i]+=score[x]
                visited[i]=True

    print(*score)

if __name__=='__main__':
    main()