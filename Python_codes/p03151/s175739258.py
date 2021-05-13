n=int(input())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
pl=[]
nl=0
ans=0
su=0
for a,b in zip(al,bl):
    su+=a-b
    if a>=b:
        pl.append(a-b) 
    else:nl+=a-b;ans+=1
if su<0:print(-1);exit()
pl.sort()


while nl<0:
    nl+=pl.pop()
    ans+=1
print(ans)