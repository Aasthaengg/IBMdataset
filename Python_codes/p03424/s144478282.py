import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    S = list(input().split())
    L = len(Counter(S))
    if L == 3:
        print('Three')
    else:
        print('Four')


if __name__ == '__main__':
    main()
