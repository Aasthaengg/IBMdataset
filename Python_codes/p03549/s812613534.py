n, m = map(int, input().split())

cost = 1900 * m + 100 * (n - m)
p = 0.5 ** m

print(int(cost/p))