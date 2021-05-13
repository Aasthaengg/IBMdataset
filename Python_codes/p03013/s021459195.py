import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
mod = 10**9+7

dp = [0]*(N+1)
dp[0] = 1
broken = set([int(input()) for _ in range(M)])
for i in range(1, N+1):
    if i in broken:
        continue
    dp[i] += dp[i-1]
    if i>=2:
        dp[i] += dp[i-2]
    dp[i] %= mod
print(dp[-1])