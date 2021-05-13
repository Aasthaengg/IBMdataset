N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
A.sort()
dp=[False]*(K+1)
dp[0]=False
for i in range(1,K+1):
    for j in range(len(A)):
        if((i-A[j])>=0):
            dp[i]= (dp[i] or (not dp[i-A[j]]))
# print(dp)
if(dp[K]==True):
    print("First")
else:
    print("Second")