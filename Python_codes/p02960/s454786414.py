s=input()

#i桁以下の数字でmodがjの数
#dp[i][j]=

dp=[[0 for _ in range(13)] for _ in range(len(s))]

MOD=10**9+7

if s[0]!="?":
    dp[0][int(s[0])]=1
else:
    for i in range(10):
        dp[0][i]=1


for i in range(1,len(s)):
    si=s[i]


    if s[i]!="?":
        #数字,300のmodをtempに
        for j in range(13):
            dp[i][(j*10+int(si))%13]+=dp[i-1][j]%MOD
    else:
        for l in range(10):
            for j in range(13):
                dp[i][(j*10+l)%13]+=dp[i-1][j]%MOD
    #print(dp[i],sum(dp[i]))



print(dp[len(s)-1][5]%MOD)




        

