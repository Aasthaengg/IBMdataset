A = list(map(str,input().split()))
if A[0][(len(A[0]))-1] == A[1][0] and A[1][(len(A[1]))-1] == A[2][0]:
  print("YES")
else:
  print("NO")