#ABC045D
from collections import defaultdict
h,w,n=map(int,input().split())
ans=defaultdict(int)
for i in range(n):
    a,b=map(int,input().split())
    for j in range(0,-3,-1):
        for k in range(0,-3,-1):
            if a+j>0 and a+j<=h-2 and b+k>0 and b+k<=w-2:
                ans[(a+j,b+k)]+=1
res=[0 for i in range(10)]
for x in ans.values():
    res[x]+=1
res[0]=((h-2)*(w-2))-sum(res[1:])
for i in range(10):
    print(res[i])