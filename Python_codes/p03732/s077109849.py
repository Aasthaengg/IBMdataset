import itertools
n, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = []
c = []
d= []
e= []
ans=0

for i in range(n):
    if a[i][0] == a[0][0]:
        b.append(a[i][1])
    elif a[i][0] == a[0][0]+1:
        c.append(a[i][1])
    elif a[i][0] == a[0][0]+2:
        d.append(a[i][1])
    else:
        e.append(a[i][1])

b.sort()
b.reverse()
c.sort()
c.reverse()
d.sort()
d.reverse()
e.sort()
e.reverse()

b = list(itertools.accumulate(b))
c = list(itertools.accumulate(c))
d = list(itertools.accumulate(d))
e = list(itertools.accumulate(e))
b.append(0)
c.append(0)
d.append(0)
e.append(0)


for i in range(len(b)):
    for j in range(len(c)):
        for k in range(len(d)):
            if a[0][0]*i+(a[0][0] +1)*j+(a[0][0] +2)*k>w:
                break
            else:
                x=(w-(a[0][0]*i+(a[0][0] +1)*j+(a[0][0] +2)*k))//(a[0][0]+3)
                ans=max(ans,b[i-1]+c[j-1]+d[k-1]+e[min(x-1,len(e)-1)])
print(ans)