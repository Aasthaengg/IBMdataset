
n = int(raw_input())
prices = [ int(raw_input()) for _ in range(n)] #.split(' '))
prices.sort()
print sum(prices[:-1]) + prices[-1] /2
