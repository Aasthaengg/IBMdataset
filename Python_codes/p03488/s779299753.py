s=input()
xy=list(map(int,input().split()))
p=[[0],[0]]
i=0
for c in s:
    if c=='F':
        p[i][-1]+=1
    else:
        i^=1
        p[i].append(0)
a=[1,1]
for i in range(2):
    s0=set((p[i][0],))
    for j in range(1,len(p[i])):
        s1=set()
        for e in s0:
            s1.add(e+p[i][j])
            s1.add(e-p[i][j])
        s0=s1
    if xy[i] not in s0:
        a[i]=0
print(['No','Yes'][all(a)])