h = list(map(int,input().split()))
mo = 0
for x in h:
  if x == 1:
    mo += 300000
  elif x == 2:
    mo += 200000
  elif x == 3:
    mo += 100000
if h[0] == h[1] == 1:
  mo += 400000
print(mo)