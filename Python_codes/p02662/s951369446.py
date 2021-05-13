import sys

LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))

def main():
    n, s = LI()
    a = LI()
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = 1

    for i in range(n):
        for w in range(s+1):
            dp[i+1][w] = 2*dp[i][w]
            if w >= a[i]:
                dp[i+1][w] += dp[i][w-a[i]]
            dp[i+1][w] %= 998244353

    print(dp[n][s])

if __name__ == '__main__':
    main()