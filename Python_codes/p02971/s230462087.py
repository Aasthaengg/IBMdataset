a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
c=max(b)
if b.count(c)>1:
    for i in range(a):
        print(c)
elif b.count(c)==1:
    d=sorted(b)
    d=d[a-2]
    e=b.index(c)
    for i in range(a):
        if i==e:
            print(d)
        else:
            print(c)