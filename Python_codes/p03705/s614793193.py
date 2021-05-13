import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())

    mi = a * (n - 1) + b
    ma = b * (n - 1) + a
    print(max(0, ma - mi + 1))


if __name__ == '__main__':
    resolve()
