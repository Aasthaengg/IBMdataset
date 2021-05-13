N=int(input())
if N==1:
  print("Hello World")
else:
  A,B=(input().split() for i in range(2));print(int(A[0])+int(B[0]))