N = int(input())
 
L = [2, 1]
 
if N == 1:
  print(1)
else:
  i = 1
  while i < N:
    L.append(L[i] + L[i-1])
    i += 1
  print(L[-1])