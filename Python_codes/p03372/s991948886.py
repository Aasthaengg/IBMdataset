import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, c = list(map(int, readline().split()))

    x = [0] * (n + 1)
    v = [0] * (n + 1)

    for i in range(1, n + 1):
        x[i], v[i] = map(int, readline().split())

    right_cum = [0] * (n + 1)
    left_cum = [0] * (n + 1)

    for i in range(1, n + 1):
        right_cum[i] = right_cum[i - 1] + v[i]
        left_cum[i] = left_cum[i - 1] + v[n - i + 1]

    right_nutritive = [0] * (n + 1)
    left_nutritive = [0] * (n + 1)
    right_max_cum = [0] * (n + 1)
    left_max_cum = [0] * (n + 1)

    for i in range(1, n + 1):
        right_nutritive[i] = right_cum[i] - x[i]
        left_nutritive[i] = left_cum[i] - (c - x[n - i + 1])
        right_max_cum[i] = max(right_max_cum[i - 1], right_nutritive[i])
        left_max_cum[i] = max(left_max_cum[i - 1], left_nutritive[i])

    r_temp = max(right_nutritive)
    l_temp = max(left_nutritive)
    ans = max(r_temp, l_temp)

    for i in range(1, n + 1):
        rl = right_nutritive[i] - x[i] + left_max_cum[n - i]
        lr = left_nutritive[i] - (c - x[n - i + 1]) + right_max_cum[n - i]
        ans = max(ans, rl, lr)

    print(ans)


if __name__ == '__main__':
    main()
