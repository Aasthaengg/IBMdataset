import random
import time
import copy

t1=time.time()
d=int(input())
c=input()
cl=[int(n) for n in c.split()]
sl=list()
for i in range(d):
    s=input()
    sl=sl+[int(n) for n in s.split()]
tl=list()
for i in range(d):
    tl.append(random.randint(1,26))
sat=0
for i in range(d):
    sat+=sl[i*26+tl[i]-1]
last=list()
for i in range(26):
    last.append([a for a, x in enumerate(tl) if x==i+1])
dec=0
for i in range(26):
    if last[i]==list():
        dec+=(d*(d+1)/2)*cl[i]
    else:
        for v in range(len(last[i])):
            if v!=len(last[i])-1:    
                dec+=cl[i]*(last[i][v+1]-last[i][v]-1)*(last[i][v+1]-last[i][v])/2
            else:
                dec+=cl[i]*(d-last[i][v]-1)*(d-last[i][v])/2
        dec+=cl[i]*(last[i][0])*(last[i][0]+1)/2
        
def dechf(c,last):
    decha=0
    if last[c]==list():
        decha+=(d*(d+1)/2)*cl[c]
    else:
        for v in range(len(last[c])):
            if v!=len(last[c])-1:    
                decha+=cl[c]*(last[c][v+1]-last[c][v]-1)*(last[c][v+1]-last[c][v])/2
            else:
                decha+=cl[c]*(d-last[c][v]-1)*(d-last[c][v])/2
        decha+=cl[c]*(last[c][0])*(last[c][0]+1)/2
    return(int(decha))


oldlast=copy.deepcopy(last)
oldans=sat-int(dec)
oldtl=copy.copy(tl)
t2=time.time()
newans=0
while t2-t1<1.85:
    if round(t2)%2==0:
        d1=random.randint(1,d)
        d2=random.randint(1,d)
        if d1==d2:
            continue
        q1=tl[d2-1]
        q2=tl[d1-1]
        cha=sl[(d1-1)*26+q1-1]-sl[(d1-1)*26+tl[d1-1]-1]+sl[(d2-1)*26+q2-1]-sl[(d2-1)*26+tl[d2-1]-1]
        c=tl[d1-1]-1
        dech=dechf(c,last)
        c=tl[d2-1]-1
        dech+=dechf(c,last)
        last[tl[d2-1]-1].remove(d2-1)
        last[tl[d1-1]-1].remove(d1-1)
        last[tl[d1-1]-1].append(d2-1)
        last[tl[d1-1]-1].sort()
        last[tl[d2-1]-1].append(d1-1)
        last[tl[d2-1]-1].sort()
        tl[d2-1]=q2
        tl[d1-1]=q1
        c=tl[d1-1]-1
        dech-=dechf(c,last)
        c=tl[d2-1]-1
        dech-=dechf(c,last)
        newans=oldans+cha+dech
    else:
        da=random.randint(1,d)
        q=random.randint(1,26)
        cha=sl[(da-1)*26+q-1]-sl[(da-1)*26+tl[da-1]-1]
        c=tl[da-1]-1
        dech=dechf(c,last)
        c=q-1
        dech+=dechf(c,last)
        last[tl[da-1]-1].remove(da-1)
        last[q-1].append(da-1)
        last[q-1].sort()
        c=tl[da-1]-1
        dech-=dechf(c,last)
        tl[da-1]=q
        c=tl[da-1]-1
        dech-=dechf(c,last)
        newans=oldans+cha+dech
    r=0
    if newans<oldans:
        if 2.7**((newans-oldans)/(1.85-(t2-t1)))<random.random():
            r=1
    if r==1:
        tl=copy.copy(oldtl)
        last=[i[:] for i in oldlast]
    else:
        oldans=newans
        oldtl=copy.copy(tl)
        oldlast=[i[:] for i in last]
    t2=time.time()
for i in range(d):
    print(tl[i])
        

