import sys
input = sys.stdin.readline
from collections import Counter, deque

INF = float('inf')

""" Input
S = input().rstrip()
N, A, B = map(int, input().split())
A = list(map(int, input().split()))
D = [int(input()) for _ in range(N)]
"""


def main():
    R = int(input())
    print(R ** 2)


if __name__ == '__main__':
    main()
