N=int(input())
res = 0
def checkOdd(N):
  k = 0
  for i in range(1,N+1):
    if N % i ==0:
      k += 1
  if k == 8:
    return True
  else:
    return False
 
if N<104:
  print(res)
else:
  for i in range(105,N+1,2):
    if checkOdd(i):
      res += 1
  print(res)