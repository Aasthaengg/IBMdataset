n,W=map(int,input().split())
wv=[list(map(int,input().split())) for _ in range(n)]
x=[[] for _ in range(4)]
w0=wv[0][0]
for w,v in wv:
    x[w-w0].append(v)
for i in range(4):
    x[i].sort()
    x[i]=x[i][::-1]
y=[[0] for i in range(4)]
for i in range(4):
    if len(x[i])>0:
        y[i].append(x[i][0])
for i in range(4):
    for j in range(1,len(x[i])):
        y[i].append(y[i][-1]+x[i][j])
res=[]
for a in range(len(x[0])+1):
    for b in range(len(x[1])+1):
        for c in range(len(x[2])+1):
            for d in range(len(x[3])+1):
                if w0*a+(w0+1)*b+(w0+2)*c+(w0+3)*d<=W:
                    res.append(y[0][a]+y[1][b]+\
                              y[2][c]+y[3][d])
print(max(res))