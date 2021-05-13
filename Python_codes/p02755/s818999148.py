import math
a,b=map(int,input().split())
x=[]
for i in range(1,1251):
    if math.floor(i*0.08)==a:
        if math.floor(i*0.1)==b:
            x.append(i)
if len(x)==0:
    print(-1)
else:
    print(min(x))