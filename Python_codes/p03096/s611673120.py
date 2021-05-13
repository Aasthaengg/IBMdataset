import sys
input = sys.stdin.readline
n=int(input())
c=[]
tmp=0
num=0
for i in range(n):
    m=int(input())
    if m!=tmp:
        c.append(m)
        tmp=m
        num+=1
n=num
from collections import Counter
dp=Counter()
ans=1
mod=10**9+7
for i in range(n):
    dp[c[i]]=(dp[c[i]]+ans)%mod
    ans=dp[c[i]]
print(ans)