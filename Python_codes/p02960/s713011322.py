import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    L = len(s)
    dp = [[0] * 13 for _ in range(L + 1)]
    dp[0][0] = 1

    for i in range(L):
        for j in range(13):
            if s[i] == "?":
                for k in range(10):
                    dp[i + 1][(j * 10 + k) % 13] += dp[i][j] % mod
            else:
                k = int(s[i])
                dp[i + 1][(j * 10 + k) % 13] += dp[i][j] % mod

    print(dp[-1][5] % mod)


if __name__ == '__main__':
    resolve()
