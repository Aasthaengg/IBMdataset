f=lambda: map(int,input().split())
    
V,E,P=f()
G=[]
for _ in range(E):
    s,t,d=f()
    G.append((s,t,-(d-P)))

INF=float('inf')
res=[INF]*(V+1)
res[1]=0

def Bellman_Ford():
    for s,t,d in G:
        res[t]=min(res[t],res[s]+d)
        
negative_flg=False
r=INF
for _ in range(V):
    tmp=res[:]
    Bellman_Ford()
    r=min(res[-1],r)
    if tmp==res:
        break
else:
    r0=res[-1]
    for _ in range(V):
        tmp=res[:]
        for s,t,d in G:
            if res[t]>res[s]+d:
                res[t]=-INF
    if r0!=res[-1]:
        negative_flg=True
if negative_flg:
    print(-1)
else:
    print(max(-r,0))