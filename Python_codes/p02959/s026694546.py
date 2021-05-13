def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        if a_list[i] >= b_list[i]:
            ans += b_list[i]
        else:
            d = b_list[i] - a_list[i]
            ans += a_list[i]
            if a_list[i + 1] >= d:
                ans += d
                a_list[i + 1] = a_list[i + 1] - d
            else:
                ans += a_list[i + 1]
                a_list[i + 1] = 0

    print(ans)


if __name__ == "__main__":
    main()
