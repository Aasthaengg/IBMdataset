import sys

input = sys.stdin.readline


def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x.append(X)
    y.append(Y)

    if max(x) < min(y):
        ans = "No War"
    else:
        ans = "War"

    print(ans)


if __name__ == "__main__":
    main()
