import sys
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = int(input())
    x1 = math.ceil(S ** 0.5)
    x2 = x1 ** 2 - S
    print(0, 0, x1, 1, x2, x1)


if __name__ == '__main__':
    main()
