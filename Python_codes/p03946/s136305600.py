N, T = map(int, input().split())
prices = map(int, input().split())


profit_memo = []
min_price = next(prices)

for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit_memo.append(price - min_price)

max_profit = max(profit_memo)
print(profit_memo.count(max_profit))
