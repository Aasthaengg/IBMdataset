N,K=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N-1)]
mod=10**9+7
fac=[1,1]
for i in range(2,K+1):
    fac.append(fac[i-1]*i%mod)
ifac=[pow(i,mod-2,mod) for i in fac]
def perm(a,b):
    if b==0:
        return(1)
    if a<b:
        return(0)
    return(fac[a]*ifac[a-b]%mod)



data=[[] for i in range(N+1)]
for a,b in AB:
    data[a].append(b)
    data[b].append(a)

"""
for i in range(1,N):
    if len(data[i])==1:
        stack=[[i,0]]
        break"""
stack=[[1,0]]
visited=set([stack[0][0]])
count=K
while stack:
    a,m=stack.pop()
    c=0
    for p in data[a]:
        if not p in visited:
            visited.add(p)
            c+=1
            stack.append([p,1])
    if c:
        count=count*perm((K-2) if m else (K-1),c)%mod

print(count)
