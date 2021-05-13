import math
N=int(input())
a=0
for i in range(1,N+1):
    if ((math.log10(i))//1)%2==0:
        a+=1
print(a)