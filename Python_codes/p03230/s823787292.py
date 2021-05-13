n=int(input())
y=(1+8*n)**0.5
if not y.is_integer():
    print("No")
    exit()
x=int(y)
if x%2==0:
    print("No")
    exit()
print("Yes")

k=(1+x)//2
atama=set()
atama.add(1)
now=1
for i in range(1,1000):
    now+=i
    if now<=n:
        atama.add(now)
    else:
        break
haji=set()
d={}
now=0
for i in range(1,1000):
    now+=i
    if now<=n and now not in haji:
        haji.add(now)
        d[now]=i
    else:
        break
k=len(atama)

ans=[list(atama),list(haji)]
for s in atama:
    if s==1:
        continue
    l=[s]
    while s+1 not in haji:
        l.append(s+1)
        s+=1
    s+=1
    l.append(s)
    c=d[s]
    for i in range(c,1000):
        s+=i
        if s<=n:
            l.append(s)
        else:
            break
    ans.append(l)
print(k+1)
for i in range(k+1):
    print(k,*ans[i])
