import sys
from math import ceil


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = int(input())
    T = [int(input()) for _ in range(5)]
    min_t = min(T)
    num = ceil(n / min_t)
    print(5 + num - 1)


if __name__ == '__main__':
    main()
