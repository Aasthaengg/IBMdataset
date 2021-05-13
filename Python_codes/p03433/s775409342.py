N = int(input())
A = int(input())

B = N//500
C = N - 500*B

if C <= A:
  print("Yes")
else:
  print("No")