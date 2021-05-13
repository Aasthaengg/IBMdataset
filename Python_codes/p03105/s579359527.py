i = list(map(int, input().split()))
A = i[0]
B = i[1]
C = i[2]
D = B // A

if D <= C:
  print(D)
else:
  print(C)
  
