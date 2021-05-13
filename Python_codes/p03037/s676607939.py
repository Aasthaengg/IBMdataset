def main():
    n, m = map(int, input().split())
    lr_lst = [list(map(int, input().split())) for _ in range(m)]
    left = 0
    right = n + 1

    for i in range(m):
        if left < lr_lst[i][0]:
            left = lr_lst[i][0]
        if lr_lst[i][1] < right:
            right = lr_lst[i][1]

    if right - left < 0:
        print(0)
    else:
        print(right - left + 1)


if __name__ == "__main__":
    main()
