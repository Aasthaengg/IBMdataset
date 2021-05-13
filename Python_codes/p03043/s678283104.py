from math import log2, ceil
n, k = map(int, input().split())
prob = [0.5**max(ceil(log2(k / i)), 0) for i in range(1, n + 1)]
print(sum(prob) / n)