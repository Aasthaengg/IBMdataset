k, x = map(int, input().split())

max_ = x + (k - 1)
min_ = x - (k - 1)

ans = list(range(min_, max_ + 1))
for i in ans:
    print(i, end = " ")