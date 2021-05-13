N = int(input())
L = [2,1,3]
if N >= 3:
  for i in range(N-2):
    L[0] = L[1]
    L[1] = L[2]
    L[2] = L[0] + L[1]
  print(L[2])
else:
  print(L[N])