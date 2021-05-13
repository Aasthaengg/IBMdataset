import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] = 1 / A[i]

    print(1/sum(A))


if __name__ == "__main__":
    main()
