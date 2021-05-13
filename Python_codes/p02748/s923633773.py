def main():
    a, b, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    xyc_lst = [list(map(int, input().split())) for _ in range(m)]

    min_a = min(a_lst)
    min_b = min(b_lst)
    ans = min_a + min_b

    for i in range(m):
        x = xyc_lst[i][0]
        y = xyc_lst[i][1]
        c = xyc_lst[i][2]

        cost = a_lst[x - 1] + b_lst[y - 1] - c

        if cost < ans:
            ans = cost

    print(ans)


if __name__ == "__main__":
    main()
