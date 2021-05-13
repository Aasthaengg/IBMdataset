import math
N=int(input())
a=[]
for i in range(1,N+1):
    if math.log2(i)%1==0:
        a.append(i)
print(a[len(a)-1])