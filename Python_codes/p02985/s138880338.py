import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N, K = map(int, readline().split())
    to = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, readline().split())
        a-=1
        b-=1
        to[a].append(b)
        to[b].append(a)

    P = int(1e9)+7
    
    #方針
    #頂点0からBFSで頂点を訪問していく
    #頂点0から順に取りうる色の種類数を決めていく
    #深さ0のとき頂点0はK色から選ぶことができる
    #左側の子から順に色を決めていく
    #深さ1の左端の頂点は頂点0で一つ使用されているのでそれ以外の色であるK-1色から選ぶ
    #深さ1の左端からi番目（左端をi=0）の頂点はK-1-i色から選ぶ

    #深さ2以降の頂点は左端の頂点に対して選択できる色はK-2色である
    from collections import deque 
    dq = deque()
    #頂点0から探索していく
    dq.append(0)
    #頂点0はK色の選択肢がある
    ans = K%P
    done = [0 for _ in range(N)]
    done[0] = 1
    #BFS
    while len(dq)>0:
        v = dq.popleft()
        i = 2
        if v == 0:
            i = 1
        for nx in to[v]:
            if done[nx] == 1:
                continue
            if K-i<=0:
                print(0)
                return
            ans *= K-i
            ans %= P
            i += 1
            done[nx] = 1
            dq.append(nx)

    print(ans)
if __name__ == '__main__':
    main()
