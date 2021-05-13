n,m,*a=map(int,open(0).read().split())
d=[]
for i,j in((7,3),(9,6),(8,7),(6,6),(5,5),(4,4),(3,5),(1,2),(2,5)):
    if i in a:
        d.append((i,j))
dp=[0]*-~n
for i in range(1,n+1):
    for j,k in d:
        if i-k<0 or i-k!=0 and not dp[i-k]:continue
        dp[i]=max(dp[i],dp[i-k]*10+j)
print(dp[n])