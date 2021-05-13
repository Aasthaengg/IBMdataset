a,b,c,d,e,f=map(int, input().split())

indxmax=0.0
wmax=0
emax=0
elimit=(100*e)/(100+e)
c31=int(f/c)+1
for ai in range(0,f+1,100*a):
    for bi in range(0,f-ai+1,100*b):
        w=ai+bi
#        print("a,b:",ai,bi,w)
        if w<=f and w>0:
            c31=(w*e)//100+c
            for ci in range(0,c31,c):
#                di=(max(0,(c31-ci-1))//d)*d
#                di=min(di,((e*w/100-ci)//d)*d)
                di=int(max(0,(min(f-w-ci,e*w/100-ci)//d)*d))
#                di=int(max(0,(min(f-w-ci-1,e*w/100-ci)//d)*d))
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