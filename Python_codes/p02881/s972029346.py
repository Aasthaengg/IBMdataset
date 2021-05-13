N = int(input())
i = 1 
res =N
flag = True
if N ==1:
  print(0)
else:
  k = int(N**0.5)
  for j in range(1,k+1):
    k = N / j
    b = int(k)
    if k-b == 0:
      res = min(res,j+b-2)
print(res)