N,W=map(int,input().split())
l=[0]*4
s=[[] for i in range(4)]
for i in range(N):
    w,v=map(int,input().split())
    if w in l:
        s[l.index(w)].append(v)
    else:
        for i in range(4):
            if l[i]==0:
                l[i]=w
                s[i].append(v)
                break
g=[[0] for i in range(4)]
for i in range(4):
    s[i].sort(reverse=1)
    t=0
    for j in s[i]:
        t+=j
        g[i].append(t)
a=0
for i in range(len(g[0])):
    for j in range(len(g[1])):
        for k in range(len(g[2])):
            for m in range(len(g[3])):
                if i*l[0]+j*l[1]+k*l[2]+m*l[3]>W:
                    continue
                t=g[0][i]+g[1][j]+g[2][k]+g[3][m]
                if t>a:
                    a=t
print(a)