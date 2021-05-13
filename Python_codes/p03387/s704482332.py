a, b, c = map(int, input().split())

res1 = a+b+c
res2 = max(a, b, c)*3
if (res2-res1)%2==0:
  print((res2-res1)//2)
else:
  res3 = (max(a, b, c)+1)*3
  print((res3-res1)//2)