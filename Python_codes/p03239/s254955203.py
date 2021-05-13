mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, T = map(int, input().split())
    ans = 10**9
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    if ans == 10**9:
        print("TLE")
    else:
        print(ans)


if __name__ == '__main__':
    main()
