
n,a,b,c=map(int,input().split())
l=[0]*n
for i in range(n):
    l[i]=int(input())
    
import itertools
 
mpmin=a+b+c+1
for i in itertools.product([0,1,2,3], repeat=n):
    aa=0
    bb=0
    cc=0
    mpa=0
    mpb=0
    mpc=0
    ia=0
    ib=0
    ic=0
    for ii in range(n):
        if i[ii]==1:
            ia=1
            if aa>0:
                mpa+=10
            aa+=l[ii]
        elif i[ii]==2:
            ib=1
            if bb>0:
                mpb+=10
            bb+=l[ii]
        elif i[ii]==3:
            ic=1
            if cc>0:
                mpc+=10
            cc+=l[ii]
    if ia==1 and ib==1 and ic==1:
        mp=mpa+abs(a-aa)+mpb+abs(b-bb)+mpc+abs(c-cc)
#        if mp<mpmin:
#            print(mp,mpa,mpb,mpc,i)
        mpmin=min(mp,mpmin)

print(mpmin)    
