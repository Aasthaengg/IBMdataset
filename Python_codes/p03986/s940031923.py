from itertools import groupby as gb
l=[(a,len(list(b))) for a,b in gb(list(input()))]
ans=0
now=0
if l[0][0]=="T":
    ans+=l[0][1]
    now+=1
pres=0
for (k,x),(k1,y) in zip(l[now::2],l[now+1::2]):
    #print(ans,pres)
    if x+pres>=y:pres=(x+pres-y)
    else:
        ans+=y-x-pres
        pres=0
print(ans+pres+(0 if l[-1][0]=="T" else l[-1][1]))