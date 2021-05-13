import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    a = int(input())

    res = n ** 2 - a
    print(res)


if __name__ == '__main__':
    resolve()
