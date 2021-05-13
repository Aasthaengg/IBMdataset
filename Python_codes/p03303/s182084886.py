import math

s = list(input())
w = int(input())
A = []
for k in range(int(math.ceil(len(s)/w))):
  A.append(s[k*w])
print(''.join(A))