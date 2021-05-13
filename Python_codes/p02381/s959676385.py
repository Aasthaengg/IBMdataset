import math as m
while True:
    x=int(input())
    if x==0:
        break
    else:
        y=list(map(int,input().split()))
        m=sum(y)/x
        a=0
        for i in range(0,x):
            r=(y[i]-m)**2
            a+=r
        a=a/x
        print(f'{a**(1/2):.8f}')
