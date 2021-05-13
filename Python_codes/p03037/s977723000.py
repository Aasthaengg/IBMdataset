def main():
    n, m = map(int, input().split())
    l_lst = [0 for _ in range(m)]
    r_lst = [0 for _ in range(m)]

    for i in range(m):
        l, r = map(int, input().split())
        l_lst[i] = l
        r_lst[i] = r

    left = max(l_lst)
    right = min(r_lst)

    if right - left < 0:
        print(0)
    else:
        print(right - left + 1)


if __name__ == "__main__":
    main()
