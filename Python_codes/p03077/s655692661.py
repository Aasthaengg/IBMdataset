import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    X = min(A, B, C, D, E)
    q, r, = divmod(N, X)
    num = q + int(r > 0)

    ans = 5 + (num - 1)
    print(ans)


if __name__ == "__main__":
    main()
