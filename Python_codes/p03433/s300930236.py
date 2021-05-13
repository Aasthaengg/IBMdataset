N = int(input())
A = int(input())
NX = N//500
NY = N - NX * 500
if NY <= A:
  print("Yes")
else:
 print("No")