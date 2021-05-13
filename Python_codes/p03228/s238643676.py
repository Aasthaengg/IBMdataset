A,B,K = map(int,input().split())
for i in range(K):
  if i%2 == 0:
    if A%2 == 1:
      A -=1
      X = A/2
      A -= X
      B += X
    else:
      X = A/2
      A -= X
      B += X
  else:
    if B%2 == 1:
      B -=1
      X = B/2
      B -= X
      A += X
    else:
      X = B/2
      B -= X
      A += X
print(int(A),int(B))