import bisect
n=int(input())
a=[int(i) for i in input().split()]
a.sort()
ans=[]
x=bisect.bisect_left(a, 0)
m=a[:x]
p=a[x:]

if n==2 and len(p)==2:
    print(p[1]-p[0])
    print(p[1],p[0])
    
    exit()
if m==[]:
    m+=[p[0]-p[-1]]
    ans+=[[p[0],p[-1]]]
    del p[0]
    del p[-1]

if p==[]:
    p+=[m[-1]-m[0]]
    ans+=[[m[-1],m[0]]]
    del m[-1]
    del m[0]

while len(p)!=1:

    m+=[m[0]-p[0]]
    ans+=[[m[0],p[0]]]
    del p[0]
    del m[0]
cnt=p[0]
for i in m:
    ans+=[[cnt,i]]
    cnt-=i
print(cnt)
for i,j in ans:print(i,j)
