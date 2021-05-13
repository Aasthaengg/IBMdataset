num = int(input())

item_prices = []

for i in range(num):
    price = int(input())
    item_prices.append(price)
    
highest_price = max(item_prices)

item_prices[item_prices.index(highest_price)] = highest_price // 2

total_price = sum(item_prices)
print(total_price)