a, b, c = map(int, input().split())

tg_c = b + c
dt_c = a + b

if c <= dt_c:
  print(tg_c)
else:
  print(a+b*2+1)