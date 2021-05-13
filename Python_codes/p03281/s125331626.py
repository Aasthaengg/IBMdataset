import math
n=int(input())
t=0

for i in range(n):
    if (i+1)%2==0:
        continue
    else :
        s=0
        for j in range(i+1):
            if (i+1)%(j+1)==0:
                s+=1
        if s==8:
            t+=1
print(t)