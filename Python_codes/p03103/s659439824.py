n,m = map(int, input().split())
l = list()
for i in range(n):
  a,b = map(int, input().split())
  l.append([a,b])
l.sort()
money = 0
for i in range(n):
  x = l[i][1]
  if m > x:
    m -= x
    money += l[i][0]*x
  else:
    money += l[i][0] * m
    break
print(money)