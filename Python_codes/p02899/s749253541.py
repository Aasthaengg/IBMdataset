import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0] * N
    for i, a in enumerate(A, 1):
        ans[a - 1] = i

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
