X=int(input())
import sys
for i in range(X,10**5+1000):
  T=True
  for j in range(2,i):
    if i%j==0:
      T=False
  if T==True:
    print(i)
    break
  else:
    continue