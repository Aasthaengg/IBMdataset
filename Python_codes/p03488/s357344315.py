s=input()
x,y=map(int,input().split())
a=[0]*8000
b=[0]*8000
tmp=0
T=True
asize=0
bsize=0
for i in s:
    if i=="T":
        tmp=1-tmp
        T=True
    elif tmp==0:
        if T:
            asize+=1
            T=False
        a[asize-1]+=1
    else:
        if T:
            bsize+=1
            T=False
        b[bsize-1]+=1
c={0}
for i in range(asize):
    d=set()
    if i==0:
        if s[0]=="T":
            d.add(-a[i])
        d.add(a[i])
    else:
        for j in c:
            d.add(j+a[i])
            d.add(j-a[i])
    c=d
if not x in c:
    print("No")
    quit()
c={0}
for i in range(bsize):
    d=set()
    for j in c:
        d.add(j+b[i])
        d.add(j-b[i])
    c=d
if not y in c:
    print("No")
    quit()
print("Yes")
