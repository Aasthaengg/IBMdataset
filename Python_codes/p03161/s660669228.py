import sys

def solve(n,k,ar):

    dp = [sys.maxsize]*n
    dp[0] = 0

    for i in range(n):
        for k in range(1,k+1):
            if i+k <= n-1:
                dp[i+k] = min(dp[i+k], dp[i] + abs(ar[i]-ar[i+k]))

    print(dp[n-1])



if __name__ == '__main__':
    n,k = map(int,input().split())
    ar = list(map(int,input().split()))

    solve(n,k,ar)