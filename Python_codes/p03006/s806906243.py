n=int(input())
dots=[]
for i in range(n):
    x,y=map(int,input().split())
    dots.append((x,y))
dots=sorted(sorted(dots, key=lambda x:x[1]))
#print(dots)
from itertools import combinations

combs=combinations(dots,r=2)
tmp=0
for c in combs:
    c=sorted(c)
    dx=c[1][0]-c[0][0]
    dy=c[1][1]-c[0][1]
    cnt=0
    for i in range(n):
        subdot=(dots[i][0]+dx,dots[i][1]+dy)
        if subdot in dots:
            cnt+=1
    tmp=max(tmp,cnt)
print(n-tmp)