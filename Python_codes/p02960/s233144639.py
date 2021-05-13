S = list(input())
N = len(S)
dp = [[0]*13 for i in range(N+1)]
dp[0][0]=1
p = 10**9+7

for i in range(1,N+1):
    X = S[N-i]
    if X=="?":
        for X in range(10):
            Y = (X*pow(10,i-1,13))%13
            for j in range(13):
                if 0<=Y+j<=12:
                    Z = Y+j
                else:
                    Z = Y+j-13
                dp[i][Z] = (dp[i][Z]+dp[i-1][j])%p
    else:
        X = int(X)
        Y = (X*pow(10,i-1,13))%13
        for j in range(13):
            if 0<=Y+j<13:
                Z = Y+j
            else:
                Z = Y+j-13
            dp[i][Z] = dp[i-1][j]
#print(*dp,sep='\n')
print(dp[-1][5])