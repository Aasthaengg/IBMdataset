N = int(input())

price_list = [int(input()) for _ in range(N)]

purchase_price = price_list[0]
profit = price_list[1] - purchase_price
for price in price_list[1:]:
    if profit < price - purchase_price:
        profit = price - purchase_price
    if price < purchase_price:
        purchase_price = price

print(profit)
