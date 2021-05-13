import math
const=3500+1
N = int(input())
ans=4/N
flg=False
for h in range(1,const):
    for n in range(h,const):
        tmp=4*h*n-N*n-N*h
        if tmp != 0:
            w = N*h*n/tmp
            if w == int(w) and w>0:
                print(h,n,int(w) )
                flg=True
                break
    if flg==True:
        break

