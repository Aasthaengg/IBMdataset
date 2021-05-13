from collections import deque
n,k=map(int,input().split())
if n==1 and k==1:
    print(1)
    exit()
if k==1:
    print(0)
    exit()
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
mod=10**9+7
ans=k
q=deque([0])
v=[0]*n
v[0]=1
vc=1
while q and vc<n:
    s=q.popleft()
    c=0
    if s==0:
        kai=k-1
    else:
        kai=k-2
    for es in g[s]:
        if v[es]==0:
            v[es]=1
            vc+=1
            c+=1
            q.append(es)
            ans*=kai
            ans%=mod
            kai-=1
print(ans%mod)
