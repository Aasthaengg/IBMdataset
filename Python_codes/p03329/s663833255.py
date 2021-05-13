import sys


def resolve():
    readline = sys.stdin.readline

    def func(n: int, a: int):
        res = 0
        while n > 0:
            res += n % a
            n = int(n / a)
        return res

    N = int(readline())

    res = N
    for i in range(N + 1):
        tmp = func(i, 6) + func(N - i, 9)
        res = min(res, tmp)
    print(res)

resolve()
