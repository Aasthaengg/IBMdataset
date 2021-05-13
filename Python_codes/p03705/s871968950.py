N,A,B = map(int,input().split())

B_max = B*(N-1)+A
A_min = A*(N-1)+B

if A>B:
  print(0)
elif A==B:
  print(1)
elif N==1:
  print(0)
else:
  print(B_max-A_min+1)