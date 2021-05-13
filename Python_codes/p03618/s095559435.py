a=input()
n=len(a)
from collections import Counter
c=Counter()
dp=[0]*(n)
dp[0]=1
c[a[0]]=1
for i in range(1,n):
    dp[i]=dp[i-1]+i-c[a[i]]
    c[a[i]]+=1
print(dp[-1])