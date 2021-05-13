A,B,K=map(int,input().split())
for i in range(K):
  if i%2==0:
    if A%2!=0:
      B += (A-1)//2
      A = (A-1)//2
    else:
      B += A//2
      A //= 2
  else:
    if B%2!=0:
      A += (B-1)//2
      B = (B-1)//2
    else:
      A += B//2
      B //= 2
print(A,B)      