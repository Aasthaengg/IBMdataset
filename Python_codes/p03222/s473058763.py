h,w,k=map(int,input().split())
ws=[0]*10
ws[0]=1
ws[1]=1
for i in range(2,10):
    ws[i]=ws[i-1]+ws[i-2]
dp=[[0 for i in range(h+1)] for j in range(w)]
dp[0][0]=1
mod=10**9+7
if w==1:
    print(1)
    exit()
for i in range(h):
    for j in range(w):
        if j==0:
            dp[0][i+1]=dp[0][i]*ws[w-1]+dp[1][i]*ws[max(0,w-2)]
            dp[0][i+1]%=mod
        elif j==w-1:
            dp[w-1][i+1]=dp[w-1][i]*ws[w-1]+dp[w-2][i]*ws[max(0,w-2)]
            dp[w-1][i+1]%=mod
        else:
            dp[j][i+1]=dp[j][i]*ws[max(0,j)]*ws[max(0,w-j-1)]+dp[j-1][i]*ws[max(0,j-1)]*ws[max(0,w-j-1)]+dp[j+1][i]*ws[max(0,j)]*ws[max(0,w-j-2)]
            dp[j][i+1]%=mod
print(dp[k-1][h]%mod)
