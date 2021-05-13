def main():
    n, m = map(int, input().split())
    ab_list = [list(map(int, input().split())) for _ in range(n)]
    cd_list = [list(map(int, input().split())) for _ in range(m)]

    for ab in ab_list:
        a = ab[0]
        b = ab[1]
        min_diff = 10 ** 9
        ans = 0
        for i in range(m):
            c = cd_list[i][0]
            d = cd_list[i][1]
            diff = abs(a - c) + abs(b - d)
            if diff < min_diff:
                min_diff = diff
                ans = i + 1
        print(ans)


if __name__ == "__main__":
    main()
