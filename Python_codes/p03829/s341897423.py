import sys

readline = sys.stdin.buffer.readline


def main():
    N, A, B = map(int, readline().split())
    X = list(map(int, readline().split()))

    c = 0
    for i in range(N - 1):
        c += min(A * (X[i + 1] - X[i]), B)

    print(c)


main()
