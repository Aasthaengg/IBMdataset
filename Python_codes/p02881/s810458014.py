import math
n=int(input())
a=int(math.sqrt(n))
for i in range(a,0,-1):
    if n%i==0:
        print(i+n//i-1-1)
        exit()
