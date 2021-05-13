import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    X_com = 0
    for i in range(1, N+1):
        X_com += (i - 1) * X[i-1] - (N - i) * X[i-1]

    Y_com = 0
    for i in range(1, M+1):
        Y_com += (i - 1) * Y[i-1] - (M - i) * Y[i-1]

    return (X_com * Y_com) % (10**9 + 7)


if __name__ == '__main__':
    print(main())
