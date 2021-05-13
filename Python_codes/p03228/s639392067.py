A,B,K=map(int,input().split())

for i in range(K):
  if i%2:
    if B%2:
      B -= 1
    A,B = A+B//2,B//2
  else:
    if A%2:
      A -= 1
    A,B = A//2,B+A//2
    
print(A,B)