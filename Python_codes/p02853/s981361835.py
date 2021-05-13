x,y = map(int, input().split())
p = [300000,200000,100000]
ot = [0]*205
dt = p+ot

if x * y == 1:
  print(dt[x-1]+dt[y-1]+400000)
else:
  print(dt[x-1]+dt[y-1])