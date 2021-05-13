N, T = map(int, input().split())
A = list(map(int, input().split()))

min_town_price = A[0]
max_profit = -1
max_profit_pairs = 0
for i in range(1, N):
    profit = A[i] - min_town_price
    if max_profit < profit:
        max_profit = profit
        max_profit_pairs = 1
    elif max_profit == profit:
        max_profit_pairs += 1
    min_town_price = min(min_town_price, A[i])
print(max_profit_pairs)
