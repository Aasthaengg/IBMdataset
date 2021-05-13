n,m=map(int,input().split())
c=list()

for i in range(m):
    c.append(list(map(int,input().split())))

s=(list(map(lambda x:x[0],c)))
b=(list(map(lambda x:x[1],c)))

maxs=max(s)
minb=min(b)

if minb<maxs:
    print('0')
else:
    ans=minb-maxs+1
    print(ans)