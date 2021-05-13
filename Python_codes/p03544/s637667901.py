s= int(input())
L0 = 2
L1 = 1
L = 0
if s ==1:
  print(L1)
else:
  for i in range(2,s+1):
    L = L0 + L1
    L0 = L1
    L1 = L
  print(L)