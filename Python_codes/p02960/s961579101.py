s = input()

dp = [[0 for i in range(13)] for j in range(len(s)+1)]
dp[0][0]=1
keta = 1
di=10**9+7
ii = len(s)
for i in range(len(s)):
    if s[ii-1-i] != "?":
        for j in range(13):
            dp[i+1][(keta*int(s[ii-1-i])+j)%13]=(dp[i+1][(keta*int(s[ii-1-i])+j)%13]+dp[i][j])%di
    else:
        for j in range(13):
            for num in range(10):
                #print(dp[i][j])
                dp[i+1][(keta*num+j)%13]=(dp[i+1][(keta*num+j)%13]+dp[i][j])%di
    keta = (keta*10)%13

#print(*dp,sep="\n")
print(dp[len(s)][5])
