def coin_change(coins, payment):
    T = [0] + [50001] * payment
    for c in coins:
        for i in range(c, payment + 1):
            T[i] = min(T[i], T[i - c] + 1)
    return T[payment]

n, m = map(int, input().split())

c = list(map(int, input().split()))

ans = coin_change(c, n)

print(ans)