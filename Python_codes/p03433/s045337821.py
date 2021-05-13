N,A = (int(input()) for i in range(2))
 
B = N % 500

if B <= A:
  print("Yes")
else:
  print("No")