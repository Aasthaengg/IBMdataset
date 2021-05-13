n=int(input())
p,m=[],[]
z=0
for i in list(map(int,input().split())):
    if i<0:m.append(i)
    elif i==0:
        z+=1
    else:p.append(i)
if p and m:
    print(sum(p)-sum(m))
    if z:
        for h in range(z-1):
            print("0 0")
        now=0
    else:now=p.pop()
    for j in m[1:]:
        print(now,j)
        now-=j
    if p:
        print(m[0],now)
        now=-now+m[0]
        for j in p[1:]:
            print(now,j)
            now-=j
        print(p[0],now)
    else:
        print(now,m[0])
elif p:
    if z:
        print(sum(p))
        for h in  range(z-1):
            print("0 0")
        now=0
        f=p.pop()
        for i in p:
            print(now,i)
            now-=i
        print(f,now)
    else:
        print(sum(p)-2*min(p))
        p.sort()
        now=p[0]
        k=p.pop()
        for j in p[1:]:
            print(now,j)
            now-=j
        print(k,now)
else:
    if z:
        print(-sum(m))
        for h in  range(z-1):
            print("0 0")
        now=0
    else:
        m.sort()
        print(-sum(m)+2*max(m))
        now=m.pop()
    for i in m:
        print(now,i)
        now-=i

