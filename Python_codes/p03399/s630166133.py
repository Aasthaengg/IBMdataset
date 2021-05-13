# input
prices = [int(input()) for n in range(4)]

# check
print(min(prices[:2]) + min(prices[2:]))