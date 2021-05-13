n,k=map(int,input().split())
td=[tuple(map(int,input().split())) for _ in range(n)]

td.sort(key=lambda x:x[1])

kind=set()

base=0
rest=[]

for i in range(k):
    t,d=td.pop()

    base+=d

    if t in kind:
        rest.append(d)
    
    kind.add(t)

cntk=len(kind)
ans=base+cntk*cntk

while len(rest)>0:
    bd=rest.pop()
    
    while len(td)>0:
        nt,nd=td.pop()
        if nt not in kind:
            break
    else:
        break

    base+=nd-bd
    cntk+=1
    ans=max(ans,base+cntk*cntk)
    kind.add(nt)

print(ans)