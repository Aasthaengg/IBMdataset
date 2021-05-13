import math
A,B,N = [int(x) for x in input().split(' ')]
if N/B >= 1:
  print(int(A+math.floor(-float(A)/float(B))))
else:
  print(int(math.floor(float(N)*float(A)/float(B))))
