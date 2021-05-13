import sys

input = sys.stdin.readline


def main():
    W, H, N = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    A = [0] * N
    for i in range(N):
        X[i], Y[i], A[i] = map(int, input().split())

    x_min = 0
    x_max = W
    y_min = 0
    y_max = H
    for x, y, a in zip(X, Y, A):
        if a == 1:
            x_min = max(x_min, x)
        elif a == 2:
            x_max = min(x_max, x)
        elif a == 3:
            y_min = max(y_min, y)
        else:
            y_max = min(y_max, y)

    ans = max(0, x_max - x_min) * max(0, y_max - y_min)
    print(ans)


if __name__ == "__main__":
    main()
