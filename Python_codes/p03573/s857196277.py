abclist=list(map(int,input().split()))
abclist.sort()

A,B,C=abclist
if A==B:
  print(C)
else:
  print(A)