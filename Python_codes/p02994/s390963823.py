n, l = map(int, input().split())

taste = [l + i - 1 for i in range(1, n + 1)]
taste_all = sum(taste)
if taste[n - 1] < 0:
    taste_min = taste[n - 1]
elif taste[0] > 0:
    taste_min = taste[0]
else:
    taste_min = 0
print(taste_all - taste_min)
