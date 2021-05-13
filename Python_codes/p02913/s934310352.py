import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
S = list(input())

dp = [[0]*(N+1) for _ in range(N+1)]
ans = 0
for i in range(1, N):
    for j in range(i+1, N+1):
        if S[i-1]==S[j-1]:
            dp[i][j] = min(dp[i-1][j-1]+1, j-i)
            ans = max(ans, dp[i][j])

print(ans)