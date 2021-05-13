import sys
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


INF = 10**18


def bfs(N, v0, goal, edge):

    dp = [[-1 for _ in range(3)] for _ in range(N)]
    dp[v0][0] = 0
    q = deque()
    q.append((v0, 0))

    while q:
        v, cnt = q.popleft()

        if cnt == 2:
            nx_cnt = 0
        else:
            nx_cnt = cnt + 1

        for nv in edge[v]:
            if dp[nv][nx_cnt] == -1:
                q.append((nv, nx_cnt))
                if cnt == 0:
                    dp[nv][nx_cnt] = dp[v][cnt] + 1
                else:
                    dp[nv][nx_cnt] = dp[v][cnt]
        # print(v, dp)

    return dp[goal][0]


def main():

    N, M = in_nn()
    edge = [[] for _ in range(N)]

    for i in range(M):
        u, v = in_nn()
        u, v = u - 1, v - 1
        edge[u].append(v)

    S, T = in_nn()
    S, T = S - 1, T - 1
    ans = bfs(N, S, T, edge)

    print(ans)


if __name__ == '__main__':
    main()
