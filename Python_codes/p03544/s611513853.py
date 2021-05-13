N = int(input())
L0 = 2
L1 = 1
if N == 1:
  print(1)
else:
  for i in range(N-1):
    L2 = L1 + L0
    L0 = L1
    L1 = L2
  print(L2)