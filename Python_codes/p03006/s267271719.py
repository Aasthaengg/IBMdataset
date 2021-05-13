N=int(input())
xy=[list(map(int,input().split()))for _ in range(N)]

count=[]
for x1,y1 in xy:
    for x2,y2 in xy:
        if x1==x2 and y1==y2:
            continue
        c=str(x1-x2)+':'+str(y1-y2)
        count.append(c)

from collections import*
C=Counter(count)
C['zentsu999']=0
print(N-max(C.values()))