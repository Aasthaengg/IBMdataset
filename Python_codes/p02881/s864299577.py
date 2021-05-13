N = int(input())
import math 

start = int(math.sqrt(N))+1
for i in range(start,0,-1):
    if N%i==0:
        print(i+N//i-2)
        break