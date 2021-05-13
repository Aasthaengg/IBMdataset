N,X=map(int,input().split())
m=[]
for i in range(N):
    m.append(int(input()))
m.sort()
a=0
if X>sum(m):
    a+=len(m)
    X-=sum(m)
    while X>=0:
        a+=1
        X-=min(m)
    print(a-1)
else:
    for i in range(N):
        a+=1
        X-=m[i]
        if X<m[i]:
            break
    print(a)