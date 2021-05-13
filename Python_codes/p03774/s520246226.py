def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    cd = [list(map(int, input().split())) for _ in range(M)]

    for s in ab:
        tmp = 10 ** 10
        ans = 0
        for i, t in enumerate(cd, 1):
            if tmp > abs(s[0]-t[0]) + abs(s[1]-t[1]):
                ans = i
                tmp = abs(s[0]-t[0]) + abs(s[1]-t[1])
        print(ans)


if __name__ == "__main__":
    main()
