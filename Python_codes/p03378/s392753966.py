N, M, X = map(int, input().split())
A = list(map(int, input().split()))

i = 0
j = 0
while 1:
  if j in A and j < X:
    i = j
    j += 1
  elif j < X:
    j += 1
  else:
    break
    
smaller = 0
bigger = 0
if i == 0:
  print(0)
else:
  for k in range(A.index(i) + 1):
    smaller += 1
  
  for k in range(A.index(i) + 1, M, 1):
    bigger += 1

  print(min(smaller, bigger))