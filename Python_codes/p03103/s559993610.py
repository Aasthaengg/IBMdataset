def main():
    n, m = map(int, input().split())
    ab_list = [list(map(int, input().split())) for _ in range(n)]
    ab_list.sort(key=lambda x: x[0])
    ans = 0

    for ab in ab_list:
        a, b = ab[0], ab[1]
        if b <= m:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break

    print(ans)


if __name__ == "__main__":
    main()
