def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())

    G = [[] for _ in range(N + 1)]

    for _ in range(M):
        l, r, d = map(int, input().split())
        G[l].append((r, -d))
        G[r].append((l, d))


    MIN = -10 ** 18

    lst = [MIN] * (N + 1)

    que = deque()
    que_append = que.append
    que_popleft = que.popleft

    for i in range(1, N + 1):
        if lst[i] == MIN:
            que_append(i)
            lst[i] = 0

        while que:
            tmp = que_popleft()
            for next_, d in G[tmp]:
                if lst[next_] == MIN:
                    lst[next_] = lst[tmp] + d
                    que_append(next_)
                    continue
                
                if lst[next_] == lst[tmp] + d:
                    continue
                else:
                    print ('No')
                    exit()

    print ('Yes')

if __name__ == '__main__':
    main()