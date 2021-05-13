n=int(input())
from collections import defaultdict
d=defaultdict(int)
for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            d[i**2+j**2+k**2+i*j+j*k+k*i]+=1
for i in range(1,n+1):
    print(d[i])