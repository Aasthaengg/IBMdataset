mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, A, B = map(int, input().split())

    if N == 1:
        if A != B:
            print(0)
        else:
            print(1)
    elif N == 2:
        print(1)
    else:
        if A <= B:
            print(B * (N-1) + A - (A * (N-1) + B) + 1)
        else:
            print(0)


if __name__ == '__main__':
    main()
