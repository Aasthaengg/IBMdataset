import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, t = map(int, input().split())
    T = list(map(int, input().split()))

    res = 0
    for i in range(n - 1):
        res += t if T[i] + t <= T[i + 1] else T[i + 1] - T[i]

    print(res + t)


if __name__ == '__main__':
    resolve()
