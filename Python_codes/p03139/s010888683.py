N,A,B = map(int,input().split())
if N < A+B:
  print(min(A,B),A+B-N)
else:
  print(min(A,B),0)