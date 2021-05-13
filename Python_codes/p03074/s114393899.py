from collections import deque
n,k=map(int,input().split())
s=input()
w=[]
f=s[0]
ans=chk=0
d=deque([])
for i in s:
    if i!=f:
        if f=='0': chk*=-1
        w.append(chk)
        f=i
        chk=1
    else:
        chk+=1
if f=='0': chk*=-1
w.append(chk)

chk=0
for i in w:
    if i>0 or k>0:
        if i<0: k-=1
        chk+=abs(i)
        d.append(i)

    elif k>0:
        chk+=abs(i)
        k-=1
        d.append(i)
    else:
        x=d.popleft()
        chk-=abs(x)
        if x>0:
            x=d.popleft()
            chk-=abs(x)
        chk+=abs(i)
        d.append(i)

    ans=max(ans,chk)

print(ans)
