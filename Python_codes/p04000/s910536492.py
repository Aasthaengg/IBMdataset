from collections import defaultdict as dd

h,w,n=map(int,input().split())
d=dd(int)
c={i:0 for i in range(10)}

for _ in range(n):
    a,b=map(int,input().split())
    for i in range(3):
        for j in range(3):
            if a-i>0 and b-j>0 and a-i<=h-2 and b-j<=w-2:
                d[(a-i,b-j)]+=1

d=dict(d)
v=0
for i in d.values():
    c[i]+=1
    v+=1
c[0]=(h-2)*(w-2)-v

for i in range(10):
    print(c[i])
