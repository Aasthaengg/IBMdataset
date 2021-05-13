from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=defaultdict(int)
for i in range(n):
    d[a[i]]+=1

for i,j in d.items():
    if j>=2:
        b.append(i)
    if j>=4:
        c.append(i)

if len(b)<2 and len(c)<1:
    print(0)
elif len(c)==1 and len(b)<2:
    print(c[0]**2)
else:
    b.sort(reverse=True)
    rec=b[0]*b[1]
    if len(c)>=1:
        c.sort(reverse=True)
        cube=c[0]**2
    else:
        cube=0
    print(max(rec,cube))