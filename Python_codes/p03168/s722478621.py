import sys
x=50000
sys.setrecursionlimit(x)

n=int(input())
arr = list(map(float,input().split()))
dp = [[-1]*(3001) for i in range(3001)]

def func(n,x):
    if x==0:
        return 1
    if dp[n][x]>-0.9:
        return dp[n][x]  
    if n==0:
        return 0
    
    dp[n][x] = (arr[n-1])*func(n-1,x-1) + (1-arr[n-1])*func(n-1,x)
    return dp[n][x]

print("%0.10f"%func(n,(n+1)//2))
