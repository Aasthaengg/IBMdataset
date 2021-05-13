mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    ans = 0
    M = -1
    for _ in range(N):
        p = int(input())
        ans += p
        if p > M:
            M = p
    print(ans - M // 2)


if __name__ == '__main__':
    main()
