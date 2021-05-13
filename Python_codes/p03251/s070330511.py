mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, M, XX, YY = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    X.append(XX)
    Y.append(YY)
    if max(X) < min(Y):
        print("No War")
    else:
        print("War")


if __name__ == '__main__':
    main()
