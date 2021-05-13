n,m=map(int,input().split())
x=[]
y=[]
for i in range(m):
    a,b=map(int,input().split())
    x.append([a,b,i])
x.sort()
s=1
for i in range(m):
    c=x[i][0]
    a=6-len(str(x[i][0]))
    b=["0"]*a
    for j in range(len(str(x[i][0]))):
        b.append(str(x[i][0])[j])
    x[i][0]="".join(b)
    a=6-len(str(s))
    b=["0"]*a
    for j in range(len(str(s))):
        b.append(str(s)[j])
    x[i].append("".join(b))
    if i<m-1:
        if c==x[i+1][0]:
            s+=1
        else:
            s=1
for i in range(m):
    y.append([x[i][2],x[i][0],x[i][3]])
y.sort()
for i in range(m):
    print(y[i][1]+y[i][2])