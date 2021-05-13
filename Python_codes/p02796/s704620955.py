N,sections=int(input()),[]

for i in [0]*N:
    x,l=map(int,input().split())
    sections.append((x+l,x-l))

sections.sort()

res=N
r,l=sections.pop(0)
for nr,nl in sections:
    if nl<r:
        res-=1
    else:
        r=nr
print(res)