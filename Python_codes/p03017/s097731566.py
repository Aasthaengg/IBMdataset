import sys
N,A,B,C,D=map(int,input().split())
S=input()
if C<D:
  for i in range(A-1,D-1):
    if S[i]=="#" and S[i+1]=="#":
      print("No")
      sys.exit()
  print("Yes")
  sys.exit()
else:
  for i in range(A-1,C-1):
    if S[i]=="#" and S[i+1]=="#":
      print("No")
      sys.exit()  
  for i in range(B-2,D-1):
    if S[i]=="." and S[i+1]=="." and S[i+2]==".":
      print("Yes")
      sys.exit()
    if i==D-2:
      print("No")
      sys.exit()
  print("Yes")
  sys.exit()