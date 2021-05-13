n,m=map(int,input().split())
l=list()
for i in range(m):
    l.append(list(map(int,input().split())))
p=0
for o in range(m):
    d={i:[] for i in range(1,n+1)}
    for i in range(m):
        if i==o:
            continue
        a,b=l[i]
        d[a].append(b)
        d[b].append(a)
    q=[1]
    s={i:1 for i in range(1,n+1)}
    while len(q)>0:
        for i in d[q.pop()]:
            if s[i]:
                s[i]=0
                q.append(i)
    #print(s)
    if 1 in s.values():
        p+=1
print(p)