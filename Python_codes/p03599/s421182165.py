a,b,c,d,e,f=map(int,input().split())

rmax=0
for a100 in range(0,f+1,100*a):
   for b100 in range(0,f-a100+1,100*b):
#   for b100 in range(0,f+1,100*b):
        if a100+b100>0:
            fcd=f-a100-b100
            for ci in range(0,fcd+1,c):
                for di in range(0,fcd+1,d):
                    if a100+b100+ci+di <=f:
                        if (a100+b100)/100*e>=ci+di:
                            if rmax<(ci+di)/(a100+b100):
                                rmax=(ci+di)/(a100+b100)
                                rab=a100+b100+ci+di
                                rcd=ci+di
if rmax>0:
    print(rab,rcd)
else:
    print(100*a,0)               