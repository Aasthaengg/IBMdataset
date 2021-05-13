from sys import stdin
def solve():
    s = int(stdin.readline())
    mod = 10**9+7
    if s < 3: return 0
    dp = [0]*(s+1)
    dp[0] = 1
    for i in range(3,s+1):
        for x in range(3,i+1):
            if x in [i-1,i-2]:
                continue
            dp[i] += dp[i-x]
    return dp[s]%mod
print(solve())