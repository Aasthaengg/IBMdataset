A,B,C,D,E,F=map(int,input().split())

w=[]
s=[]
for i in range(F):
    for j in range(F):
        a=100*A*i
        b=100*B*j
        if (a+b)>F:
            continue

        w.append(a+b)

for i in range(F):
    for j in range(F):
        c=C*i
        d=D*j
        if (c+d)>F:
            continue
        s.append(c+d)
ans=0.0
l=[100*A,0]
for water in w:
    for sugar in s:
        p=water+sugar
        if p==0:
            continue
        if p>F:
            continue 
        val=sugar/p
        if val<=(E/(100+E)):
            if ans<val:
                ans=val
                l=[p,sugar]

print(*l)