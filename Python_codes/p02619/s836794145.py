def score(tl,sl,cl):
    sat=0
    last=[0]*26
    satl=list()
    for i in range(365):    
        sat+=sl[i*26+tl[i]-1]
        dec=0
        for l in range(26):
            if l+1!=tl[i]:  
                last[l]+=1
                dec+=cl[l]*last[l]
            else:
                last[l]=0
        sat-=dec
        satl.append(sat)
    return(satl)







d=int(input())
c=input()
cl=[int(n) for n in c.split()]
sl=list()
for i in range(365):
    s=input()
    sl=sl+[int(n) for n in s.split()]
tl=list()
for i in range(365):
    t=int(input())
    tl.append(t)
for i in range(365):
    print(score(tl,sl,cl)[i])
