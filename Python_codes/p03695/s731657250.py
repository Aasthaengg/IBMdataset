n,*a=map(int,open(0).read().split())

rank=[0]*9

for aa in a:
    rank[aa//400 if aa<3200 else 8]+=1

cnt=8
for i in range(8):
    if rank[i]==0:
        cnt-=1

print('{} {}'.format(max(1,cnt),cnt+rank[8]))