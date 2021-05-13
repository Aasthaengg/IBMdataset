import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = 1
    for i in range(n):
        res *= i + 1
        res %= mod

    print(res)


if __name__ == '__main__':
    resolve()
