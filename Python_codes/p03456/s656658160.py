import math
a, b = input().split()
N = int(a+b)
flag = False
for i in range(math.ceil(math.sqrt(N))):
  if (i+1)**2 == N:
    flag = True
    break
if (flag):
  print("Yes")
else:
  print("No")