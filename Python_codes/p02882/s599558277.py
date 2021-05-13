import sys
from math import atan, degrees

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    a, b, x = map(int, readline().split())

    if x > a * a * b / 2:
        ans = atan(2 * (a * a * b - x) / (a ** 3))
    else:
        ans = atan(a * b * b / (2 * x))

    print(degrees(ans))
    return


if __name__ == '__main__':
    main()
