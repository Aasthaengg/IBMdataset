N,W=map(int,input().split())
w=[0]*N;v=[0]*N
for i in range(N):w[i],v[i]=map(int,input().split())
V=[[] for _ in [0]*4]
for i in range(N):V[w[i]-w[0]].append(v[i])
for i in range(4):
    V[i].sort(reverse=True)
    for j in range(len(V[i])-1):V[i][j+1]+=V[i][j]
    V[i].insert(0,0)

a=0
for i in range(len(V[0])):
    for j in range(len(V[1])):
            for k in range(len(V[2])):
                for l in range(len(V[3])):
                    if i*w[0]+j*-~w[0]+k*-~-~w[0]+l*-~-~-~w[0]<=W:a=max(a,V[0][i]+V[1][j]+V[2][k]+V[3][l])
print(a)