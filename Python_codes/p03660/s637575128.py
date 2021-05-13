import sys
sys.setrecursionlimit(10**7)

def tree(p):
    for x in neighbor[p]:
        if x==par[p]: continue
        par[x]=p
        descend[p]+=tree(x)
    return descend[p]

n=int(input())
neighbor=[[]  for _ in range(n+1)]
descend=[1]*(n+1)
par=[0]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    neighbor[a].append(b)
    neighbor[b].append(a)
tree(1)

x=[descend[n]-1]
t=n
while t!=1:
    t,pret=par[t],t
    x.append(descend[t]-descend[pret]-1)

l=len(x)
p,q=sum(x[:l//2]),sum(x[l//2:])
if l%2==0: print("Fennec" if p<q else "Snuke")
else: print("Fennec" if p<=q else "Snuke")