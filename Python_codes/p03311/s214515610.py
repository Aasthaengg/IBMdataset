import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = [a - i for i, a in enumerate(A, start=1)]
    A.sort()

    b = A[(N + 1) // 2 - 1]
    ans = sum(map(lambda x: abs(x - b), A))
    print(ans)


if __name__ == "__main__":
    main()
