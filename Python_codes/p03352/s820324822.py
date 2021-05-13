from math import *
x=int(input())
ans=[]
if x<4:
    print(1)
    exit()
for i in range(2,int(sqrt(x))+1):
    t=2
    while i**t<=x:
        ans.append(i**t)
        t+=1
print(max(ans))