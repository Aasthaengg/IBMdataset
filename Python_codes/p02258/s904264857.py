import sys


fin = sys.stdin.readline
n = int(fin())
price_list = [int(fin()) for _ in range(n)]
min_price_so_far = float('inf')
max_profit = float('-inf')
for price in price_list:
    profit = price - min_price_so_far
    max_profit = max(max_profit, profit)
    min_price_so_far = min(min_price_so_far, price)
print(max_profit)

