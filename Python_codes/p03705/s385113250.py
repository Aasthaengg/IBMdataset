N,A,B = map(int,input().split())
P = A*(N-1)+B
Q = B*(N-1)+A
if P <= Q:
  print(Q - P +1)
else:
  print(0)