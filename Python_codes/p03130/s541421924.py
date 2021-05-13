AB = [list(map(int,input().split())) for _ in [0]*3]

E = [[] for _ in [0]*4]
for a,b in AB:
    a-=1
    b-=1
    E[a].append(b)
    E[b].append(a)

i = 0
for _ in [0]*2:
    d = [-1]*4
    d[i] = 0
    q = [i]
    while q:
        i = q.pop()
        for j in E[i]:
            if d[j]!= -1 : continue
            d[j] = d[i]+1
            q.append(j)
print("YES" if max(d)==3 else "NO")