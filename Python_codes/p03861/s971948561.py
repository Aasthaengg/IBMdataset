import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, x = map(int, input().split())

    res_a = (a - 1) // x
    res_b = b // x
    print(res_b - res_a)


if __name__ == '__main__':
    resolve()
