import sys
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    X = int(readline())
    print(360//math.gcd(360,X))


if __name__ == '__main__':
    main()
