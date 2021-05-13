mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    a, b = map(int, input().split())
    P = list(map(int, input().split()))
    x = y = z = 0
    for p in P:
        if p <= a:
            x += 1
        elif a < p <= b:
            y += 1
        else:
            z += 1
    print(min(x, y, z))


if __name__ == '__main__':
    main()
