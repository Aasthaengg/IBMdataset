N,M = map(int,input().split())
LRD = [list(map(int,input().split())) for _ in [0]*M]

E = [{} for _ in [0]*N]
for L,R,D in LRD:
    E[L-1][R-1] = D
    E[R-1][L-1] = -D

V = [None]*N
breakFlg = False
for i in range(N):
    if V[i]!=None:
      	continue
    V[i] = 0
    q = [i]
    while q:
        j = q.pop()
        v = V[j]
        for k,d in E[j].items():
            if V[k] == None:
                V[k] = v+d
                q.append(k)
ans = True
for l,e in enumerate(E):
    for r,d in e.items():
        ans = ans and V[r]-V[l]==d
    if not ans:
      	break
print("Yes" if ans else "No")
