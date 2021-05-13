import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = input_int()
    MOD = 10**9 + 7
    dp = [0] * 2010
    dp[0] = 1
    dp[1] = 0
    dp[2] = 0
    for i in range(3, S + 1):
        dp[i] = (dp[i - 3] + dp[i - 1]) % MOD
    print(dp[S])
    return


if __name__ == "__main__":
    main()
