mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    d = 10000000
    ans = 0
    for i, h in enumerate(H):
        if abs(T - 0.006*h - A) < d:
            d = abs(T - 0.006*h - A)
            ans = i+1
    print(ans)


if __name__ == '__main__':
    main()
