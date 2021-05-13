h,w,n=map(int,input().split())
spots=set([eval(input().replace(' ','*w+'))-w-1 for i in range(n)])
anss=[0]*10
from itertools import product as pr
moves=(tuple(x+w*y for x,y in pr(range(0,3),repeat=2)))
for i in spots:
    a,b=divmod(i,w)
    pre=[0]*9
    for x in range(max(0,a-2),min(h-2,a+1)):
        for y in range(max(0,b-2),min(w-2,b+1)):
            ind=w*x+y
            pre[x-a+(y-b)*3+8]+=sum(ind+m in spots for m in moves)
    for v in pre:anss[v]+=1
tans=[0]*10

ans0=(h-2)*(w-2)
for i in range(1,10):
    tans[i]=anss[i]//i
    ans0-=anss[i]//i
tans[0]=ans0
print(*tans,sep='\n')
