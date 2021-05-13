a,b=map(int,input().split())
A=[int(x) for x in input().split()]
A.sort()
if a>=b:
  print(sum(A[:(a-b)]))
else:
  print(0)