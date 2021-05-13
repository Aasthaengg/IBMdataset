import sys
sys.setrecursionlimit(10**9)


N, M = map(int, input().split())
to = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    to[x - 1].append(y - 1)

# dp[i] : iを始点とする最長経路
dp = [0] * N
seen = [0] * N

def dfs(v):
    if seen[v]:
        return dp[v]
    seen[v] = 1
    res = 0
    for nv in to[v]:
        res = max(res, dfs(nv) + 1)
    dp[v] = res
    return res


def main():
    ans = 0
    for i in range(N):
        ans = max(ans, dfs(i))
    print(ans)


if __name__ == "__main__":
    main()