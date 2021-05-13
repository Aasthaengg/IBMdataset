import sys
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    H = int(readline())
    W = int(readline())
    N = int(readline())
    print(math.ceil(N/max(H,W)))


if __name__ == '__main__':
    main()
