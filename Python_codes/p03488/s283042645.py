s=input()
x,y=map(int,input().split())
xx,yy=[],[]
w=[0,0]
ans=chk=f=0
for i in s:
    if f==1 and i=='F':
        chk+=1
    elif f==1 and i=='T':
        yy.append(chk)
        f=0
    elif f==0 and i=='F':
        chk+=1
    elif f==0 and i=='T':
        xx.append(chk)
        f=1
    if i=='T': chk=0
if chk and f==1:
    yy.append(chk)
elif chk and f==0:
    xx.append(chk)
if s[0]=='F':
    w[0]+=xx[0]
    xx[0]=0
xx.sort()
yy.sort()
for i in xx[::-1]:
    if w[0]<x:
        w[0]+=i
    else:
        w[0]-=i
for i in yy[::-1]:
    if w[1]<y:
        w[1]+=i
    else:
        w[1]-=i
print("Yes" if w[0]==x and w[1]==y else "No")