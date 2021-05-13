# dp
import sys
from collections import defaultdict

stdin = sys.stdin
 
ni = lambda:int(ns())
na = lambda:list(map(int,stdin.readline().split()))
ns = lambda:stdin.readline().rstrip()  # ignore trailing spaces

MOD = 10 ** 9 + 7
d = dict()

N = ni()
C = [ni() for _ in range(N)]
dp = [1] * N
d[C[0]] = 0

for i in range(1, N):
    c = C[i]
    dp[i] = dp[i-1]
    if c in d:
        if d[c] != i-1:
            dp[i] += dp[d[c]]
    d[c] = i
    dp[i] %= MOD

print(dp[N-1])

