a, b, c, k = map(int, input().split())
print(k if k <= a else a if k <= a + b else a - (k - a - b))