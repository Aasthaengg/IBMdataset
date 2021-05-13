A,B,C,D=map(int,input().split())
if abs(A-C)<=D or (abs(A-B)<=D and abs(B-C)<=D):
  print("Yes")
else:
  print("No")