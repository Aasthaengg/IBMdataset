import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = input().rstrip()
    B = input().rstrip()
    C = input().rstrip()

    ans = 0
    for a, b, c in zip(A, B, C):
        ans += len(set([a, b, c])) - 1

    print(ans)


if __name__ == "__main__":
    main()
