def main():
    n, m, x = map(int, input().split())
    book_list = [list(map(int, input().split())) for _ in range(n)]
    ans = 12 * 10 ** 5 + 1

    for i in range(2 ** n):
        money = 0
        level = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                money += book_list[j][0]
                for k in range(m):
                    level[k] += book_list[j][k + 1]
        for j in range(m):
            if level[j] < x:
                break
        else:
            ans = min(ans, money)

    if ans == 12 * 10 ** 5 + 1:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()
