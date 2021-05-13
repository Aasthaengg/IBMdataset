import numpy as np
t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
y1=a1*t1-b1*t1
y2=a2*t2-b2*t2
if y1 == -y2:
    print('infinity')
else:
    if y1<0:
        y1*=-1
        y2*=-1
    n=int(np.trunc(y2/(y1+y2)))
    if n<1:
        print(0)
    elif(y2/(y1+y2)==n):
        print((n-1)*2)
    else:
        print((n-1)*2+1)