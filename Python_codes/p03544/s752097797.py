N = int(input())
if N == 1:
  print(1)
else:
  L0 = 2
  L1 = 1
  for i in range(1, N):
    Ln = L0 + L1
    L0 = L1
    L1 = Ln
  print(L1)