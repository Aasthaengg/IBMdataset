a,b,c=map(int,input().split())
A=[a,b,c]
B=sorted(A)
if B[2]==B[0]+B[1]:
  print("Yes")
else:
  print("No")