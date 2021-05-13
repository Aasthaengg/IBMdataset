MOD=10**9+7

S=input()
S=S[::-1]
N=len(S)

def POWt(N):
    arr=[1]
    for i in range(1,N+1):
        arr.append(arr[-1]*10%13)
    return arr

dp=[[0]*13 for i in range(N+1)]
dp[0][0]=1
POW=POWt(N)
for i in range(N):
    for j in range(13):
        if(S[i]!='?'):
            dp[i+1][(j+(int(S[i])*POW[i]%13))%13]=(dp[i+1][(j+(int(S[i])*POW[i])%13)%13]+dp[i][j])%MOD
        else:
            for k in range(10):
                dp[i+1][(j+k*POW[i]%13)%13]=(dp[i+1][(j+k*POW[i]%13)%13]+dp[i][j])%MOD
print(dp[N][5])