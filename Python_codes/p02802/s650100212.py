n,m=list(map(int,input().split()))
ps=[input().split() for _ in range(m)]
plst=[0]*n
penlst=[0]*n
pen=0
ans=0

for p,s in ps:
    p=int(p)-1
    if plst[p]:
        continue
    if s=='AC':
        ans+=1
        pen+=penlst[p]
        plst[p]=1
    else:
        penlst[p]+=1

print('{} {}'.format(ans,pen))