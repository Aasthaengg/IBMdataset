import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, read().split())
    a = {int(read()) - 1 for _ in range(m)}
    if n == 1:
        print(1)
        return
    mod = 10**9 + 7
    dp = [0] * n
    if 0 not in a:
        dp[0] = 1
    if 1 not in a:
        dp[1] = 1 + dp[0]
    for i in range(2, n):
        if i in a:
            continue
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[-1])


if __name__ == '__main__':
    main()
