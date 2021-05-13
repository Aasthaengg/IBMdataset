from collections import deque, defaultdict
import sys
input = sys.stdin.readline


def main():
    inf = 10 ** 10
    N, M = map(int, input().split())
    x = [inf] * (N + 1)
    adj = defaultdict(lambda: [])
    for _ in range(M):
        L, R, D = map(int, input().split())
        adj[L].append((R, D))
        adj[R].append((L, -D))
    seen = [0] * (N + 1)

    def dfs(adj, start):
        que = deque()
        que.append(start)
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

    for i in range(1, N + 1):
        if seen[i] == 0:
            dfs(adj, i)

    print('Yes')


if __name__ == '__main__':
    main()
