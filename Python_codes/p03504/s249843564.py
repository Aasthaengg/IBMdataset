n,C = map(int,input().split())
st = [[] for _ in range(C)]
st2 = [[] for _ in range(C)]

for _ in range(n):
    s,t,c = map(int,input().split())
    st[c-1].append((s,t))

for i in range(C):
    st[i].sort()

for i,e in enumerate(st):
    s1 = -1
    t1 = -1
    for j in e:
        if s1 == -1:
            s1 = j[0]
            t1 = j[1]
        else:
            if j[0] == t1:
                t1 = j[1]
            else:
                st2[i].append((s1-1,t1))
                s1 = j[0]
                t1 = j[1]
    if s1 != -1:
        st2[i].append((s1-1,t1))

imos = [0]*(2*10**5+10)

for i in st2:
    for j in i:
        imos[int(j[0]*2)] += 1
        imos[int(j[1]*2)] -= 1

for i in range(2*10**5+5):
    imos[i+1] += imos[i]

print(max(imos))
