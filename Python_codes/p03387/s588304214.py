a,b,c=map(int,input().split())
L=[a,b,c]
ma = max(L)
mi = min(L)
if sum(L)%2 == ma%2:
  print((3*ma-sum(L))//2)
else:
  ma += 1
  print((3*(ma)-sum(L))//2)