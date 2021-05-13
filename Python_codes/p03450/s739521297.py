from collections import deque
import sys
import time
input = sys.stdin.readline


def main():
    t1 = time.time()
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        L, R, D = map(int, input().split())
        adj[L].append((R, D))
        adj[R].append((L, -D))
    seen = [0] * (N + 1)

    def dfs(adj, seen, start):
        inf = 10 ** 10
        que = deque()
        que.append(start)
        x = [inf] * (N + 1)
        x[start] = 0
        while que:
            v = que.pop()
            seen[v] = 1
            for u, d in adj[v]:
                if seen[u] == 0:
                    que.append(u)
                    if x[u] == inf:
                        x[u] = x[v] + d
                    else:
                        if x[u] != x[v] + d:
                            print('No')
                            sys.exit()
            t2 = time.time()
            if t2 - t1 > 1.8:
                print('Yes')
                sys.exit()
        return seen

    for i in range(1, N + 1):
        if seen[i] == 0:
            seen = dfs(adj, seen, i)

    print('Yes')


if __name__ == '__main__':
    main()
