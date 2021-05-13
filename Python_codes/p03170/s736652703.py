N, K = map(int, input().split())
a = list(map(int, input().split()))
dp=[0 for i in range(K+1)] 

for k in range(a[0],K+1):
    for n in range(N):
        if k-a[n]>=0 and dp[k-a[n]]==0:
            dp[k]=1
    
if dp[K]==1:
    print('First')
else:
    print('Second')