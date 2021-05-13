import math

N = int(input())
X = 0
a = 0
for i in range(50000):
  X = math.floor(1.08*i)
  if(X==N):
    print(i)
    a+=1
    break
if(a ==0):
  print(":(")