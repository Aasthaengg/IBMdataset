from operator import itemgetter
n,m=map(int,input().split())
a=[]
for i in range(m):
    pi,yi=map(int,input().split())
    a.append([i,pi,yi])
b=[]
c=[]
for i in range(n):
    b.append([])
    c.append([])
for i in range(m):
    x=a[i][0]
    y=a[i][2]
    b[a[i][1]-1].append([x,y])

for i in range(n):
    b[i].sort(key=itemgetter(1))
    l=len(b[i])
    for j in range(l):
        a[b[i][j][0]].append(j+1)
for i in range(m):
    xi=a[i][1]
    yi=a[i][3]
    print('{0:06d}{1:06d}'.format(xi,yi))

