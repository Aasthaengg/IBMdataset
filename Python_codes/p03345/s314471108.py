import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, k = map(int, input().split())
    res = a - b
    op = 1 if k % 2 == 0 else -1
    if abs(res) > 10 ** 18:
        print("Unfair")
    else:
        print(res * op)


if __name__ == '__main__':
    resolve()
