import sys

input = sys.stdin.readline


def main():
    A, B, K = map(int, input().split())

    a = [i for i in range(A, A + K) if i <= B]
    b = [i for i in range(B - K + 1, B + 1) if A <= i]

    ans = sorted(set(a + b))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
