a,b,c,d,e,f=map(int,input().split())

waterL=[]
ac=0
while a*100*ac<=f:
    bc=0
    while a*100*ac+b*100*bc<=f:
        waterL.append(a*100*ac+b*100*bc)
        bc += 1
    ac += 1
waterL.remove(0)
ma=0
ms=0
mw=0
for w in waterL:
    lim=w/100*e
    cc=0
    while c*cc<=lim and c*cc+w<=f:
        dc=0
        while cc*c+dc*d<=lim and c*cc+d*dc+w<=f:
            s=c*cc+d*dc
            per=s/(w+s)
            if per>=ma:
                ma=per
                ms=s
                mw=w
            dc += 1
        cc += 1
print(int(ms+mw),int(ms))