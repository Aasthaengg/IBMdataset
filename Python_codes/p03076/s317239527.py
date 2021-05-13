def main():
    cost_list = [int(input()) for _ in range(5)]
    amari_list = [cost % 10 for cost in cost_list]

    last_order = 0
    min_amari = 10
    for index, amari in enumerate(amari_list):
        if amari == 0:
            continue
        if amari < min_amari:
            min_amari = amari
            last_order = index

    ans = 0
    for index, cost in enumerate(cost_list):
        if index == last_order:
            ans += cost_list[index]
        else:
            if cost % 10 == 0:
                ans += cost
            else:
                cost = (cost // 10 + 1) * 10
                ans += cost

    print(ans)


if __name__ == "__main__":
    main()
