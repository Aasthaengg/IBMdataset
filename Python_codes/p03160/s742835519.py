import sys
N=int(input())
A=[int(i) for i in input().split()]
if N==1:
    print(0)
    sys.exit()
dp=[0]*N
dp[0]=0
dp[1]=abs(A[0]-A[1])
for i in range(2,N):
    dp[i]=min(abs(A[i]-A[i-2])+dp[i-2],abs(A[i]-A[i-1])+dp[i-1])
print(dp[-1])
    
    
