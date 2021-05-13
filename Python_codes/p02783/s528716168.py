a,b=map(int,input().split())
res =0
while a > 0:
  a += -b
  res += 1
print(res)