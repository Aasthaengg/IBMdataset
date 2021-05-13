N=int(input())
V=[[i,N//2*2-i+1] for i in range(1,N//2+1)]
if N&1:
    V+=[[N]]
E=[]
for u in range(len(V)):
    for v in range(len(V)):
        if u!=v:
            for x in V[u]:
                for y in V[v]:
                    if x<y:
                        E.append((x,y))
print(len(E))
for x,y in E:
    print(x,y)