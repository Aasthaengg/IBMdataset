mod=10**9+7
s=input()
n=len(s)
dp=[[0]*4 for _ in range(n+1)]
abc="ABC"
dp[n][3]=1
for i in range(n-1,-1,-1):
    for j in range(4):
        if j==3:
            m=0
            if s[i]=="?":
                m=3
            else:
                m=1
            dp[i][j]=(m*dp[i+1][j])%mod
        else:
            m1=0
            m2=0
            if s[i]=="?":
                m1=3
                m2=1
            else:
                m1=1
                if s[i]==abc[j]:
                    m2=1
                else:
                    m2=0
            dp[i][j]=(m1*dp[i+1][j]+m2*dp[i+1][j+1])%mod
print(dp[0][0])
