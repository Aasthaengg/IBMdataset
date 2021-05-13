n = int(input())
money = 0
for i in range(n):
    x,u = input().split()
    if u == 'BTC':
        money += float(x)*380000
    else:
        money += int(x)
print(money)
