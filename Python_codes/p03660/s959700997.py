import sys
sys.setrecursionlimit(10**7)

def cur(p):
    for x in neighbor[p]:
        if x==par[p]: continue
        else:
            par[x]=p
            descend[p]+=cur(x)
    neighbor[p].remove(par[p])
    return descend[p]

n=int(input())
neighbor=[[]  for _ in range(n+1)]
descend=[1]*(n+1)
par=[0]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    neighbor[a].append(b)
    neighbor[b].append(a)
neighbor[1].append(0)
cur(1)


x=[descend[n]-1]
t=n
while t!=1:
    t,pret=par[t],t
    x.append(descend[t]-descend[pret]-1)

l=len(x)
p,q=sum(x[:l//2]),sum(x[l//2:])
if l%2==0: print("Fennec" if p<q else "Snuke")
else: print("Fennec" if p<=q else "Snuke")