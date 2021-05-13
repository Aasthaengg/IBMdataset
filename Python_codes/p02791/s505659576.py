def main():
    n = int(input())
    p_lst = list(map(int, input().split()))

    min_val = n + 1
    ans = 0

    for i in range(n):
        if min_val >= p_lst[i]:
            min_val = p_lst[i]
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
