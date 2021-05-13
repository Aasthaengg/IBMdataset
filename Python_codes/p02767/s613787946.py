def main():
    n = int(input())
    x_lst = list(map(int, input().split()))
    ans = 10 ** 12

    for p in range(1, 101):
        sum_hp = 0
        for x in x_lst:
            sum_hp += (x - p) ** 2
        if sum_hp < ans:
            ans = sum_hp

    print(ans)


if __name__ == "__main__":
    main()
