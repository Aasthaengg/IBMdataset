N= int(input())
L0=2
L1=1
if N == 0:
  print(2)
elif N == 1:
  print(1)
else:
  for i in range(2,N+1):
    L=L0+L1
    L0 = L1
    L1 = L
  print(L)