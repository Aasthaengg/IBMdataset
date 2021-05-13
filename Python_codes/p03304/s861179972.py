import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, d = map(int, input().split())
    print((m - 1) / n if d == 0 else (m - 1) * (n - d) * 2 / pow(n, 2))


if __name__ == '__main__':
    resolve()
