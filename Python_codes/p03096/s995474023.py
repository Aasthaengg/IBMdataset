import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
mod = 10**9+7

last = {}
dp = [0]*(N+1)
dp[0] = 1
for i in range(1, N+1):
    dp[i] = dp[i-1]
    c = int(input())
    if c in last and last[c]+1<i:
        dp[i] += dp[last[c]]
        dp[i] %= mod
    last[c] = i

print(dp[N])