def main(n, l_r):
    ans = 0

    for l, r in l_r:
        ans += r - (l - 1)

    print(ans)


if __name__ == "__main__":
    n = int(input())
    l_r = [list(map(int, input().split())) for _ in range(n)]

    main(n, l_r)
