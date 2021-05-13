import sys
N,k=map(int,input().split())
A=[int(i) for i in input().split()]
if N==1:
    print(0)
    sys.exit()
dp=[0]*N
dp[0]=0
for i in range(1,N):
    j=1
    ans=float('inf')
    while True:
        if j<=k and i-j>=0:
            ans=min(abs(A[i]-A[i-j])+dp[i-j],ans)
            j+=1
        else:
            break
    dp[i]=ans
##print(dp)
    
print(dp[-1])
    
    
