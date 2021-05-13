import math
n=int(input())
x=0
for i in range(n):
    if math.sqrt(n-i)%1==0.0:
        break
    else:
        x+=1
print(n-x)