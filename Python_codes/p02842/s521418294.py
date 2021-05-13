import math
N = int(input())
A = N/1.08 
B = (N+1)/1.08 

if math.ceil(N/1.08) < math.ceil((N+1)/1.08 ):
  print(math.ceil(N/1.08))
else:
  print(':(')
