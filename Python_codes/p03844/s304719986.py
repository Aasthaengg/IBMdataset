
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    fomula = input()
    print(eval(fomula))


if __name__ == '__main__':
    resolve()
