l=[]
for i in range(3):
    x,y=map(int,input().split())
    l.append(x)
    l.append(y)
d=[]
d.append(l.count(1))
d.append(l.count(2))
d.append(l.count(3))
d.append(l.count(4))
if(max(d)==3):
    print("NO")
else:
    print('YES')