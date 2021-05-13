n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
from collections import Counter
dp=[0]*(n+1)
for x in a:
    if x!=1 and dp[x-1]!=0:
        dp[x]=dp[x-1]
    elif x!=1:
        dp[x]=x
    else:
        dp[1]=1

c=Counter(dp)
_, most=c.most_common()[0]

print(n-most)