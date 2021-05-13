N=int(input())
U=list(map(int,input().split()))
M=int(input())
T=list(map(int,input().split()))

#S = [[0 for j in range(3)] for i in range(2)]　2行3列の場合
dp = [[-1 for j in range(400001)] for i in range(N+1)]


def func(i,X,U,dp):
    if i==0:
        if X==0:
            return True
        else:
            return False
    if X<0:
        return False
    
    if dp[i][X] !=-1:
        return dp[i][X]
    
    
    if func(i-1,X,U,dp):
        dp[i][X]=1
        return dp[i][X]
    if (func(i-1,X-U[i-1],U,dp)):
        dp[i][X]=1
        return dp[i][X]
    
    dp[i][X]=0
    return dp[i][X]

for i in range(M):
    if func(N,T[i],U,dp)==True:
        print("yes")
    else:
        print("no")
