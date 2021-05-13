import sys
sys.setrecursionlimit(10**6)


def dfs(v):
    global dp
    if dp[v] != -1:
        return dp[v]
    res = 0
    for next_v in e[v]:
        res = max(dfs(next_v) + 1, res)
    dp[v] = res
    return res


def main():
    N, M = map(int, input().split())
    global e
    e = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        e[u].append(v)
    global dp
    dp = [-1]*N
    ans = -1
    for v in range(N):
        ans = max(ans, dfs(v))
    print(ans)


if __name__ == "__main__":
    main()
