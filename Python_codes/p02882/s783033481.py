import sys
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    a, b, x = map(int, readline().split())
    V = a * a * b / 2
    if V < x:
        ans = math.degrees(math.atan((2 * (a * a * b - x)) / a ** 3))
    else:
        ans = math.degrees(math.atan((a * b * b) / (2 * x)))
    print(ans)


if __name__ == '__main__':
    main()
