mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    if N == 1:
        print("Hello World")
    else:
        a = int(input())
        b = int(input())
        print(a+b)


if __name__ == '__main__':
    main()
