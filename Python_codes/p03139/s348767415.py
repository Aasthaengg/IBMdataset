N,A,B = map(int,input().split())
X = 0
if N<A+B:
  X = A+B-N
else:
  X = 0
print(min(A,B),X)