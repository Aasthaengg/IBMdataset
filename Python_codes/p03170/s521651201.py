n,k=map(int,input().split())
*a,= map(int,input().split())
a=sorted(a)
limit=10**5+5
dp=[False]*limit

for i in range(limit):
    if dp[i]==False:
        for j in range(n):
            if i+a[j]<limit:
                dp[i+a[j]]=True
if dp[k]:
    print('First')
else:
    print('Second')