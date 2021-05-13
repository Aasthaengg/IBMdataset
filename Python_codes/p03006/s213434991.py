N=int(input())
x=[list(map(int,input().split())) for _ in range(N)]

v={}
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        vect=[x[i][0]-x[j][0],x[i][1]-x[j][1]]
        vs=str(vect[0])+","+str(vect[1])
        if vs in v:
            v[vs]+=1
        else:
            v[vs]=1

VM=0
for m in v:
    VM=max(VM,v[m])
print(N-VM)