from collections import defaultdict
n,m=map(int,input().split())
a=list(map(int,input().split()))
d=defaultdict(int)
a.sort()

for i in range(m):
    b,c=map(int,input().split())
    d[c]+=b

d_sorted=sorted(d.items(),reverse=True, key=lambda x:x[0])
l=[]

for i,j in d_sorted:
    for k in range(j):
        l.append(i)
        if len(l)>n:
            break
    else:
        continue
    break
for i in range(min(n, len(l))):
    a[i]=max(a[i],l[i])

print(sum(a))