import sys
input = sys.stdin.readline

def main():
    n,s = map(int,input().split())
    a = list(map(int,input().split()))

    mod = 998244353

    dp = [[0]*s for _ in range(n)]

    for i in range(n):
        if a[i]-1 < s:
            dp[i][a[i]-1] += pow(2,i,mod)
            dp[i][a[i]-1] %= mod

    for i in range(n):
        for j in range(s):
            if i != n-1:
                dp[i+1][j] += dp[i][j] * 2
                dp[i+1][j] %= mod
            if i != n-1 and j + a[i+1] < s:
                dp[i+1][j+a[i+1]] += dp[i][j]
                dp[i+1][j+a[i+1]] %= mod

    print(dp[-1][-1]%mod)

if __name__ == '__main__':
    main()
