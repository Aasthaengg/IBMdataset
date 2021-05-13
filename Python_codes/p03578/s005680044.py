N=int(input())
D=list(map(int,input().split()))
M=int(input())
T=list(map(int,input().split()))

E={}
for d in D:
    if d in E:
        E[d]+=1
    else:
        E[d]=1

U={}
for t in T:
    if t in U:
        U[t]+=1
    else:
        U[t]=1

F=True
for u in U:
    if u in E:
        F&=(U[u]<=E[u])
    else:
        F=False

if F:
    print("YES")
else:
    print("NO")
