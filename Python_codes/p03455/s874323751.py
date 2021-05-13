import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print("Even" if a * b % 2 == 0 else "Odd")


if __name__ == '__main__':
    resolve()
