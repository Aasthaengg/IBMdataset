A = list(map(int,input().split()))
A = sorted(A)
if (A[-1]*3 -sum(A))%2 == 0:
  print((3*A[-1]-sum(A))//2)
else:
  print((3*(A[-1]+1)-sum(A))//2)