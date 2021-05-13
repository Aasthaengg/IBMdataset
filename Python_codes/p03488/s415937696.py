s=input()+"T"
X,Y=map(int,input().split())
xy=[[],[]]
t=0
m=0
for i in s:
    if(i=="T"):
        xy[m].append(t)
        m^=1
        t=0
    else:
        t+=1
x,y=xy
l=[x[0]]
s=set()
for i in x[1:]:
    s.clear()
    for j in l:
        s.add(j+i)
        s.add(j-i)
    l=list(s)
if(not X in l):
    print("No")
    quit()
l=[0]
for i in y:
    s.clear()
    for j in l:
        s.add(j+i)
        s.add(j-i)
    l=list(s)
if(not Y in l):
    print("No")
else:
    print("Yes")