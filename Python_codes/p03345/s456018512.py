mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    a, b, c, k = map(int, input().split())
    if k & 1:
        print(b-a)
    else:
        print(a-b)


if __name__ == '__main__':
    main()
