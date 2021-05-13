import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    c = [-1]
    prev = -1
    for i in range(n):
        x = int(readline())
        if x != prev:
            c.append(x)
            prev = x

    l = len(c)

    dp = [0] * l
    dp[0] = 1

    idx = dict()

    for i in range(1, l):
        char = c[i]
        dp[i] += dp[i - 1]
        if idx.get(char):
            p = idx[char]
            dp[i] += dp[p]
        idx[char] = i
        dp[i] %= MOD

    print(dp[l - 1])


if __name__ == '__main__':
    main()
