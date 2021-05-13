import math
import sys
N=int(input())
sum=0
if N==1:
    print(1)
    sys.exit()
for i in range(1,N+1):
    if i%2==1:
        sum+=1
print(sum/N)