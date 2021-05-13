import sys

input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())
    K = int(input())

    ans = A + B + C + max(A, B, C) * (2 ** K - 1)

    print(ans)


if __name__ == "__main__":
    main()
