mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    S = input().rstrip('\n')
    a = S.find("C")
    b = S.rfind("F")
    if 0 <= a < b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
