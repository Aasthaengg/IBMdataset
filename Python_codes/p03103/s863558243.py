def actual(N, M, AB):
    payment = 0

    shop_order_by_price_desc = sorted(AB, key=lambda x: x[0])

    for price, stock in shop_order_by_price_desc:
        if stock >= M:
            # 端数があるときは、残りの必要分だけ買えばよい
            return payment + (price * M)
        else:
            # 端数がないなら買い切る
            M -= stock
            payment += price * stock


N, M = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

print(actual(N, M, AB))
