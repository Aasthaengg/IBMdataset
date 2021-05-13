x = [int(i) for i in input().split()]

A = x[0]
B = x[1]
C = x[2]
D = x[3]

L = A + B
R = C + D

if L == R:
  print('Balanced')
  
elif L > R:
  print('Left')
  
else:
  print('Right')