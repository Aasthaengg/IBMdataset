import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    res = 0
    for i in range(k, n + 2):
        mi = (i - 1) * i // 2
        ma = (n + (n - i + 1)) * i // 2
        res += ma - mi + 1
        res %= mod
    print(res)


if __name__ == '__main__':
    resolve()
