import sys
from decimal import Decimal

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ave = sum(A) / Decimal(N)
    min_diff = 100
    for i, a in enumerate(A):
        if abs(ave - a) < min_diff:
            min_diff = abs(ave - a)
            ans = i

    print(ans)


if __name__ == "__main__":
    main()
