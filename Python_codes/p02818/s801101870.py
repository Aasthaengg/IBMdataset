A, B, K = map(int, input().split())

if K<=A:
  print(A-K, B)
elif A<K<=(A+B):
  print(0, B-(K-A))
else:
  print(0,0)
"""
for k in range(K):
  if A>0 and B!=0:
    A+=-1
  elif A==0 and B>0:
    B+=-1
  elif A==0 & B==0:
    break
print(A, B)
"""

