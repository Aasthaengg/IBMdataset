N=int(input())
L=[1]
now=6
while now<=10**6:
    L.append(now)
    now*=6
now=9
while now<=10**6:
    L.append(now)
    now*=9
#print(L)
dp=[float("INF")]*(N+1)
dp[0]=0
for i in range(1,N+1):
    for x in L:
        if i-x>=0:
            dp[i]=min(dp[i], dp[i-x]+1)
print(dp[N])
#print(dp)