import math
n=int(input())
k=(2*n+0.25)**0.5-0.5
k=math.ceil(k)
no=k*(k+1)/2-n
for i in range(1,k+1):
    if i==no:
        continue
    print(i)
