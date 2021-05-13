import sys
L=list()
N=int(input())
for i in range(N):
  a=int(input())
  L.append(a)
L=sorted(L)
c=sum(L)
if c%10!=0:
  print(c)
  sys.exit()
for i in range(N):
  if L[i]%10!=0:
    print(c-L[i])
    sys.exit()
print(0)