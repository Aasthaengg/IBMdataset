N=int(input())
X=set(str(N))
Y=len(X)
if Y==1:
  print(N)
if Y!=1:
  Z=0
  for i in range(111,1000,111):
    if N-i<0:
      Z+=i
      break
  print(Z)
