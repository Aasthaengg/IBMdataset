A = sorted(map(int,input().split()))
a = A[-1]//2
if A[-1] % 2 == 0:
  print(0)
else:
  print(1*A[0]*A[1])