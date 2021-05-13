import math
import copy
 
def secize(n, k):
    n2=bin(n)
    n3=n2[2:]
    for i in range(k-len(n2)+2):
        n3='0'+n3
    return n3
 
 
n=int(input())
alist = list(map(int,input().split()))
saidai=max(alist)
keta=math.ceil(math.log(saidai+1, 2))
blist=[]
for i in range(n):
    kaz=secize(alist[i], keta)
    blist.append(kaz)
 
now1=0
now2=0
nowarr=[]
for bl in blist[0]:
    nowarr.append(int(bl))
answer=0
swit=0
while now1<=n-2 and now2<=n-2:
    """
    maearr=copy.deepcopy(nowarr)
    for i in range(keta):
        if blist[now2+1][i]=='1':
            if nowarr[i]==1:
                swit=1
            else:
                nowarr[i]=1
    """
    for i in range(keta):
        if blist[now2+1][i]=='1':
            if nowarr[i]==1:
                swit=1
            else:
                nowarr[i]=2
    if swit==1:
        for i in range(keta):
            if nowarr[i]==2:
                nowarr[i]=0
        answer+=(now2-now1+1)
        #nowarr=maearr
        for i in range(keta):
            if blist[now1][i]=='1':
                nowarr[i]=0
        if now1==now2:
            nowarr=[]
            for bl in blist[now1+1]:
                nowarr.append(int(bl))
            now1+=1
            now2+=1
            if now1==n-1:
                answer+=1
        else:
            now1+=1
        swit=0
    else:
        for i in range(keta):
            if nowarr[i]==2:
                nowarr[i]=1
        if now2!=n-2:
            now2+=1
        else:
            wa=now2-now1+2
            answer+=(wa*(wa+1)//2)
            now2+=1
 
#print(now1, now2)
if n!=1:
    print(answer)
else:
    print(1)