s=input()
len_s=len(s)
mod=10**9+7
dp=[[0]*13 for i in range(len_s)]

if s[-1]!='?':
    dp[0][int(s[-1])%13]=1
else:
    for i in range(10):
        dp[0][i]=1

a=1
for i in range(1,len_s):
    a=10*a%13
    if s[-(i+1)]!='?':
        temp_S=int(s[-(i+1)])
        amari=(temp_S*a)%13
        for j in range(13):
            dp[i][(amari+j)%13]+=dp[i-1][j]%mod

    else:
        for k in range(10):
            amari=(k*a)%13
            for l in range(13):
                dp[i][(amari+l)%13]+=dp[i-1][l]%mod
#print(*dp,sep='\n')
print(dp[-1][5]%mod)
