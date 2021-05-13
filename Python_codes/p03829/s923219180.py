import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))
    answer = 0
    for i in range(1, N):
        if (X[i] - X[i - 1]) * A < B:
            answer += (X[i] - X[i - 1]) * A
        else:
            answer += B
    print(answer)


if __name__ == "__main__":
    main()
