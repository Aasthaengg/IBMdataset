import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input().rstrip()
    print(s if len(s) == 2 else s[::-1])


if __name__ == '__main__':
    resolve()
