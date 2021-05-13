import sys
import math
sys.setrecursionlimit(10**6)

N = int(input())

INF = 10**10

dp = [0]*(N+1)

for i in range(N+1):
    dp[i] = INF
    
W = [1,6,9]

def rec(v):
    if dp[v] < INF:
        return dp[v]
    if v == 0:
        dp[v] = 0
        return 0
    
    # v-n を再帰
    res = INF
    for w in range(3):
        for x in range(int(math.log(N+1,6))+1):
            n = W[w]**x
            if v<n:
                continue
            res = min(res,rec(v-n) + 1)
            # メモして返す
            dp[v] = res
    return res
rec(N)
print(dp[N])