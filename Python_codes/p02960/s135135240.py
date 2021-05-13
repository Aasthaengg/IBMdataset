import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():

    S = input()
    S = S[::-1]
    MOD = 10 ** 9 + 7

    dp = [0] * 13
    dp[0] = 1

    mul = 1
    for i in range(len(S)):
        next_dp = [0] * 13
        if S[i] == '?':
            for k in range(10):
                for j in range(13):
                    jj = ((k * mul) + j) % 13
                    next_dp[jj] += dp[j]
                    next_dp[jj] %= MOD
        else:
            num = int(S[i])
            for j in range(13):
                jj = ((num * mul) + j) % 13
                next_dp[jj] += dp[j]
                next_dp[jj] %= MOD

        mul = mul * 10 % 13
        dp = next_dp

    print(dp[5])


if __name__ == '__main__':
    solve()
