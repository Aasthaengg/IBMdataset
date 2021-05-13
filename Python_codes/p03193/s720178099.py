mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, H, W = map(int, input().split())
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        if a >= H and b >= W:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
