A = list(map(int,input().split()))
B = list(set(A))
if A.count(B[0]) == 1:
  print(B[0])
else:
  print(B[1])