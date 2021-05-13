N = int(input())
L0 = 2
L1 = 1

if N==1:
  print(1)

else:
  for n in range(N-1):
    L = L0+L1
    L0 = L1
    L1 = L
  print(L)