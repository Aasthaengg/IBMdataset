a,b=map(int,input().split())
res = 0
if a == 0:
  if b == 100:
    res = 101
  else:
    res = b
elif a == 1:
  if b == 100:
    res = 10100
  else:
    res =100*b
else:
  if b == 100:
    res = 1010000
  else:
    res =10000*b
print(res)