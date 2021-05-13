r=int(input())
A=['ABC','ARC','AGC']
if r in range(1200):
  print(A[0])
elif r in range(1200,2800):
  print(A[1])
else:
  print(A[2])