import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, t = map(int, readline().split())
    a = list(map(int, readline().split()))

    cum_max = [0] * n
    cum_max[-1] = a[-1]

    for i in range(n - 2, -1, -1):
        cum_max[i] = max(cum_max[i + 1], a[i])

    profit = [0] * n
    for i in range(n-1):
        profit[i] = cum_max[i+1] - a[i]

    print(profit.count(max(profit)))


if __name__ == '__main__':
    main()
