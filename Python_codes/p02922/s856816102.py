import math
A, B = map(int,input().split())
for i in range(30):
  if (B==1):
    print(0)
    break
  if ((A-1)*i + A >= B):
    print(i+1)
    break