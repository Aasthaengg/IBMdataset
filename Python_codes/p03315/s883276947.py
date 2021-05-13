import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    print(s.count("+") - s.count("-"))


if __name__ == '__main__':
    resolve()
