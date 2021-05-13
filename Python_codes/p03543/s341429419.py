N = int(input())
 
A = N // 1000
B = (N % 1000) // 100
C = (N % 100) // 10
D = N % 10

if A==B and B==C:
  print('Yes')
elif B==C and C==D:
  print('Yes')
else:
  print('No')
