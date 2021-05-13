B=list(input())
A=int(input())
l=""
import math
for i in range(math.ceil(len(B)/A)):
   l+=B[i*A]
print(l)