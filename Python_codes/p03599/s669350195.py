a,b,c,d,e,f=map(int, input().split())

indxmax=0.0
wmax=0
emax=0
elimit=(100*e)/(100+e)
c31=int(f/c)+1
for ai in range(0,f+1,a):
    for bi in range(0,f-ai+1,b):
        w=100*ai+100*bi
#        print("a,b:",ai,bi,w)
        if w<=f and w>0:
#            c31=int(w/100*e/c)+1
#            c31=min(int(w/100*e/c)+1,31)
#            d31=int(w/100*e/d)+1
            c31=(w*e)//100+c
            for ci in range(0,c31,c):
#                for di in range(d31):
                for di in range(0,c31-ci,d):
                    indx=(ci+di)*100/w
                    if indxmax<indx and e-indx>=0.0 and w+ci+di<=f:
                        wmax=w+ci+di
                        indxmax=indx 
                        emax=ci+di
#                    print("c,d",ci,di,emax,wmax,diii)
if wmax>0:
    print(wmax,emax)
else:
    print(100*a,emax)
