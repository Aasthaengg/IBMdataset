n=int(input())
A=[int(input()) for _ in range(n)]
H=[a for a in A if a%2==0]
if len(H)==n:
  print("second")
else:
  print("first")