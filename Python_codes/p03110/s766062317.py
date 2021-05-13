price=0
for _ in range(int(input())):
  a,b=input().split()
  if b=='JPY': price+=float(a)
  else: price+=float(a)*380000
print(price)