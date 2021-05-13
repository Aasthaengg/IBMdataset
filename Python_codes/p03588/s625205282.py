import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    x = max(A)
    y = B[A.index(x)]
    ans = x + y

    print(ans)


if __name__ == "__main__":
    main()
