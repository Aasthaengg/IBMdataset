N,K = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]

prices.sort()

print(sum(prices[:K]))
