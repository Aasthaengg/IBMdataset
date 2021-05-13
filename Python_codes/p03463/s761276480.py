mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, a, b = map(int, input().split())
    if (b-a)%2==0:
        print("Alice")
    else:
        print("Borys")


if __name__ == '__main__':
    main()
