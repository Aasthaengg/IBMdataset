import sys

input = sys.stdin.readline


def main():
    N = int(input())
    D, X = map(int, input().split())
    A = [None] * N
    for i in range(N):
        A[i] = int(input())

    ans = X
    for a in A:
        q, r, = divmod(D - 1, a)
        ans += q + 1

    print(ans)


if __name__ == "__main__":
    main()
