h,a=map(int,input().split())
res = 0
unko = h
while unko > 0:
  unko -= a
  res += 1
print(res)