n = int(input())
a = list(map(int, input().split()))

# 貪欲法
# a[i] < a[i+1]なら全部買う
# a[i] > a[i+1]なら全部売る

money = 1000
stock = 0
for i in range(n):
    if i == n-1 or a[i] > a[i+1]:
        money += stock * a[i]
        stock = 0
    elif money > a[i]:
        stock = money // a[i]
        money = money % a[i]

print(money)