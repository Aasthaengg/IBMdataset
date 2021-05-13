prices = list(map(int, input().split()))
prices.sort()
print(sum(prices[0:2]))