import math
x=int(input())
ans=0
if x<=3:
    print(1)
    exit()
for i in range(2,int(math.sqrt(x)//1)+1):
    j=2
    tmp=i**j
    while tmp<x:
        tmp=i**j
        j+=1
        if tmp<=x and tmp>ans:
            ans=tmp
print(ans)  