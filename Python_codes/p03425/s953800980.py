N=int(input())
T=set(['M','A','R','C','H'])
d={}

for _ in range(N):
    s=input()[0]
    if s in T:
        d[s]=d.get(s, 0)+1

k=len(d.keys())
ans=0
if 3<=k:
    import itertools
    for x,y,z in itertools.combinations(d.keys(), 3):
        #print(x,y,z,d[x]*d[y]*d[z])
        ans+=d[x]*d[y]*d[z]
print(ans)