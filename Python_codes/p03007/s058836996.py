n=int(input())
a=list(map(int,input().split()))
a.sort()
l=[a[0]]
r=[a[-1]]
for i in range(1,n-1):
    if a[i]<=0:
        r.append(a[i])
    else:
        l.append(a[i])
r.sort()
l.sort()
if len(r)==1:
    X=r[0]
    p=[]
else:
    p=[[r[-1],r[-2]]]
    for i in range(len(r)-3,-1,-1):
        p.append([p[-1][0]-p[-1][1],r[i]])
    X=p[-1][0]-p[-1][1]
if len(l)==1:
    Y=l[0]
    q=[]
else:
    q=[[l[0],l[1]]]
    for i in range(2,len(l)):
        q.append([q[-1][0]-q[-1][1],l[i]])
    Y=q[-1][0]-q[-1][1]
print(X-Y)
if p and q:
    for i in range(len(p)):
        print(*p[i])
    for i in range(len(q)):
        print(*q[i])
    print(X,Y)
elif p:
    for i in range(len(p)):
        print(*p[i])
    print(X,Y)
elif q:
    for i in range(len(q)):
        print(*q[i])
    print(X,Y)
else:
    print(X,Y)