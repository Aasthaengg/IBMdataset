import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

n,s=l_in()
A=l_in()


dp = [[0]*(s+1) for _ in range(n+1)]

dp[0][0]=1


mod = 998244353

for i in range(1,n+1):
    for w in range(0,s+1):
        dp[i][w] = dp[i-1][w]*2
        a = A[i-1]
        if w >= a:
            dp[i][w] += dp[i-1][w-a]

        dp[i][w] =         dp[i][w]%mod


print(dp[n][s])
