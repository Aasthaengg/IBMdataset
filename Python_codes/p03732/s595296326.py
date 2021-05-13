#060-D
n,w=map(int,input().split())
v=[[] for i in range(4)]
w1,v1=map(int,input().split())
v[0].append(v1)
for i in range(1,n):
    tw,tv=map(int,input().split())
    v[tw-w1].append(tv)
for i in range(4):
    v[i].sort(reverse=True)
cum=[[0] for i in range(4)]
for i in range(4):
    for j in range(len(v[i])):
        cum[i].append(cum[i][j]+v[i][j])
s=0
for i in range(len(v[0])+1):
    for j in range(len(v[1])+1):
        for k in range(len(v[2])+1):
            for l in range(len(v[3])+1):
                if w1*(i+j+k+l)+j+2*k+3*l>w:
                    continue
                s=max(s,cum[0][i]+cum[1][j]+cum[2][k]+cum[3][l])
print(s)