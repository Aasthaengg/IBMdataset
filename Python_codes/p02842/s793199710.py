import math
N=int(input())
X=N/1.08
X=math.ceil(X)
if math.floor(X*1.08)==N:
  print(X)
else:
  print(":(")