N=int(input())
A=list(map(int,input().split()))
m,p=[],[]
for i in A:
    if i>=0:
        p.append(i)
    else:
        m.append(i)
if m and p:
    print(sum(p)-sum(m))
    t=m[0]
    for i in p[:-1]:
        print(t,i)
        t-=i
    print(p[-1],t)
    t=p[-1]-t
    for i in m[1:]:
        print(t,i)
        t-=i
elif p:
    p.sort()
    print(sum(p[1:])-p[0])
    t=p[0]
    for i in p[1:-1]:
        print(t,i)
        t-=i
    print(p[-1],t)
else:
    m.sort(reverse=1)
    print(m[0]-sum(m[1:]))
    t=m[0]
    for i in m[1:]:
        print(t,i)
        t-=i