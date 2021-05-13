# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    n,m,*C = map(int, read().split())

    # dp[i] := i円を作るのに必要な最小枚数
    dp = [10**10] * (n+1)
    dp[0] = 0

    for c in C:
        for i in range(n+1):
            if i + c <= n:
                dp[i+c] = min(dp[i] + 1, dp[i+c])

    print(dp[n])


if __name__ == "__main__":
    main()
