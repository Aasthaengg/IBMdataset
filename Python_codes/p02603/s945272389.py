n = int(input())
a = list(map(int, input().split()))

money = 1000
for x, y in zip(a[:-1], a[1:]):
    if x < y:
        stocks = money // x
    else:
        stocks = 0
    money += (y - x) * stocks

print(money)