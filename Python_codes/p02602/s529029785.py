import sys
import decimal

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    ans = []
    x = decimal.Decimal(1)
    for i in range(N - K):
        prev = x
        x *= decimal.Decimal(A[i + K])
        x /= decimal.Decimal(A[i])
        if x > prev:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
