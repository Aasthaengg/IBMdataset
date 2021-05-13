import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())

    if b - a == c - b:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
