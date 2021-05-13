
n=int(input())
arr = list(map(float,input().split()))
dp = [[-1]*(n+1) for i in range(n+1)]
def func(n,x):
    for i in range(0,n+1):
        for j in range(0,n+1):
            if j==0:
                dp[i][j] = 1
            elif i==0:
                dp[i][j]=0
            else:
                p=(arr[i-1])*dp[i-1][j-1]
                q=(1-arr[i-1])*dp[i-1][j]
                dp[i][j] = p+q 
    
    return dp[n][x]

print("%0.10f"%func(n,(n+1)//2))