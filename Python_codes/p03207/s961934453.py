n = int(input())
goods = []
pay = 0
for i in range(n):goods.append(int(input()))
goods.sort(key=int)
pay += (goods[-1] / 2)
goods.pop(-1)
for i in range(len(goods)):
    pay += goods[i]
print(round(pay))
