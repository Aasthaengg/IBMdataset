s=input()
x,y=map(int,input().split())
lx=[]
ly=[]
t=0
k=0
for i in s:
    if i=="F":
        t+=1
    else:
        if k:
            ly.append(t)
            k=0
        else:
            lx.append(t)
            k=1
        t=0
if k:
    ly.append(t)
else:
    lx.append(t)
x-=lx.pop(0)
sx,sy={0},{0}
for i in lx:
    t=set()
    for j in sx:
        t.add(i+j)
        t.add(j-i)
    sx=t
for i in ly:
    t=set()
    for j in sy:
        t.add(i+j)
        t.add(j-i)
    sy=t
if x in sx and y in sy:
    print("Yes")
else:
    print("No")