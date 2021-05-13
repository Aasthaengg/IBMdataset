def actual(N):
    # 0 <= ケーキの数   <= N/4
    # 0 <= ドーナツの数 <= N/7
    # その範囲で (ケーキの数A, ドーナツの数B) を全探索する
    # N = 4A + 7B を満たす組があれば Yes
    n_max_cakes = N // 4
    n_max_donuts = N // 7

    for n_cakes in range(n_max_cakes + 1):
        for n_donuts in range(n_max_donuts + 1):
            price = (4 * n_cakes) + (7 * n_donuts)

            if price == N:
                return 'Yes'

    return 'No'

N = int(input())
print(actual(N))