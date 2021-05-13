mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    x, y = map(int, input().split())
    if x % y == 0:
        print(-1)
    else:
        print(x)


if __name__ == '__main__':
    main()
