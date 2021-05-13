X=int(input())
res=0
for b in range(1,1000):
  for p in range(2,1000):
    if b**p<=X :
      res=max(res,b**p)
    else:
      break
print(res)