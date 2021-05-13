#create date: 2020-07-01 11:19

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, k = na()
    r, s, p = na()
    t = ns()
    ans = 0
    for j in range(k):
        m = (n-j-1)//k+1
        dp = [[0]*m for _ in range(3)]
        o = t[j]
        if o=="s":
            dp[0][0] = r
        if o=="r":
            dp[1][0] = p
        if o=="p":
            dp[2][0] = s
        for i in range(1, m):
            o = t[k*i+j]
            premax = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
            if o == "s":
                dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + r
                dp[1][i] = premax
                dp[2][i] = premax
            if o == "r":
                dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + p
                dp[0][i] = premax
                dp[2][i] = premax
            if o == "p":
                dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + s
                dp[0][i] = premax
                dp[1][i] = premax
        ans += max([dp[0][-1], dp[1][-1], dp[2][-1]])
    print(ans)


if __name__ == "__main__":
    main()