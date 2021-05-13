import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    w, h, x, y = map(int, input().split())

    print(w * h / 2, int(x * 2 == w and y * 2 == h))


if __name__ == '__main__':
    resolve()
