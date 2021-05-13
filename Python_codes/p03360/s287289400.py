import sys

input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())
    K = int(input())

    max_v = max(A, B, C)

    ans = sum((A, B, C)) - max_v + max_v * 2 ** K
    print(ans)


if __name__ == "__main__":
    main()
