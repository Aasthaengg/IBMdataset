s=input().split("T")
X,Y=map(int,input().split())
x=list(map(len,s[::2]))
y=list(map(len,s[1::2]))
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