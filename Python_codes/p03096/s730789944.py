from collections import defaultdict
import bisect
mod = 10**9+7
N = int(input())
S = []
s = ''
for i in range(N):
    c = input()
    if s != c:
        S.append(c)
    s = c

d = defaultdict(lambda:[])
dd = defaultdict(lambda:{})
dcum = defaultdict(lambda:[0])
for i in range(len(S)):
    d[S[i]].append(i)
    dd[S[i]][i] = len(d[S[i]])-1
    dcum[S[i]].append(0)
n = len(S)
dp = [0]*(n+1)
dp[-1]=1

for i in range(n-1,-1,-1):
    l = d[S[i]]
    j = dd[S[i]][i]+1
    dp[i] += dp[i+1]
    dp[i] += dcum[S[i]][j]
    dp[i] %= mod
    dcum[S[i]][j-1] += dp[i+1]+dcum[S[i]][j]
print(dp[0])