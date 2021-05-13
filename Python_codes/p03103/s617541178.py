n, m = map(int, input().split())
l = [list(map(int,input().split())) for i in range(n)]

l.sort()

drink = 0
shop = 0
money = 0
while drink < m:
  if l[shop][1] == 0:
    shop += 1
  else:
    drink += 1
    money += l[shop][0]
    l[shop][1] -= 1
"""    
    print("shop:",shop)
    print("drink:",drink)
    print("money:",money)
"""
print(money)