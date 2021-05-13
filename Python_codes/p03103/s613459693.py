def resolve():
    N, M = map(int, input().split())

    shops = []
    for i in range(N):
        aa, bb = map(int, input().split())
        shops.append([aa, bb])

    shops.sort(key=lambda x: x[0])

    rem = M
    ans = 0
    for shop in shops:
        buy = min(rem, shop[1])
        ans += buy * shop[0]
        rem -= buy

    print(ans)


resolve()
