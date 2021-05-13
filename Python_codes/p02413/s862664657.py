r,c=map(int,input().split())
s=[]
t=[]
for i in range(r):
    s.append(list(map(int,input().split())))
    s[i].append(sum(s[i]))
for j in range(c+1):
    u = 0
    for k in range(r):
        u += s[k][j]
    t.append(u)
    s.append(t)
for i in range(r+1):
    w = str(s[i][0])
    for j in range(1,c+1):
        w += " "+str(s[i][j])
    print(w)

