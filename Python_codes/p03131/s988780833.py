import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k, a, b = map(int, input().split())

    if b - a < 2 or k - a < 1:
        print(k + 1)
    else:
        k -= a - 1
        q, k = divmod(k, 2)
        res = a + q * (b - a) + k
        print(res)


if __name__ == '__main__':
    resolve()
