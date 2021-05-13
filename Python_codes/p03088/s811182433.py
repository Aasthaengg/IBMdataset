import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

import itertools

def check(s):
    if "AGC" in s:
        return False
    for i in range(len(s)-1):
        a = s[:i] + s[i+1] + s[i] + s[i+2:]
        if "AGC" in a:
            return False
    return True

N = int(readline())
dp = [[0]*61 for i in range(N-2)]
for i in range(61):
    dp[0][i] = 1

rel = {}
cnt = 0
L = list("AGCT")
for v in itertools.product(L,repeat=3):
    s = ''.join(v)
    if check(s):
        rel[s] = cnt
        cnt += 1

for i in range(N-3):
    for k,v in rel.items():
        for s in L:
            if check(k+s):
                dp[i+1][rel[k[1:]+s]] = (dp[i+1][rel[k[1:]+s]] + dp[i][v])%mod
ans = 0
for i in range(61):
    ans = (ans + dp[N-3][i])%mod
print(ans)
