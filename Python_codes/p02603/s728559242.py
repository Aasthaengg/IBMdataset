n = int(input())
a = list(map(int, input().split()))
money = 1000
stock = 0

if a[0] <= a[1]:
    stock = money // a[0]
    money -= stock * a[0]

for i in range(1, n-1):
    if a[i] <= a[i-1] and a[i] <= a[i+1] and stock == 0:
        stock = money // a[i]
        money -= stock * a[i]
    if a[i] >= a[i-1] and a[i] >= a[i+1] and stock != 0:
        money += stock * a[i]
        stock = 0
if stock > 0:
    money += stock * a[-1]
    stock = 0
print(money)