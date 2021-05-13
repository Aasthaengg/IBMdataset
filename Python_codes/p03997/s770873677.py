import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = int(input())
    b = int(input())
    h = int(input())

    res = ((a + b) * h) // 2
    print(res)


if __name__ == '__main__':
    resolve()
