n = int(input())
a = list(map(int, input().split()))
money = 1000
stock = 0
for i in range(n-1):
    if a[i+1] > a[i]:
        stock = money // a[i]
        money += (a[i+1] - a[i]) * stock
print(money)
