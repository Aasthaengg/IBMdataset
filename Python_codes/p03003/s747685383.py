
# start:2020-05-28 00:22:02
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

MOD = 10**9+7
dp = [[0]*(M+1) for _ in range(N+1)]
rui = [[0]*(M+1) for _ in range(N+1)]
ans = 1
for i in range(N):
    for j in range(M):
        if S[i]==T[j]:
            dp[i+1][j+1] = rui[i][j] + 1
            dp[i+1][j+1] %= MOD
            ans += dp[i+1][j+1]
            ans %= MOD    
        rui[i+1][j+1] = rui[i+1][j] + rui[i][j+1] - rui[i][j] + dp[i+1][j+1]
        rui[i+1][j+1] %= MOD

print(ans)