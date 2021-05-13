h,w=map(int,input().split())
used=[[0]*w for _ in range(h)]

grid=[]

for i in range(h):
    for j in range(w):
        if used[i][j]==0:
            grid.append([(i,j)])
            used[i][j]=1
            if used[h-i-1][j]==0:
                grid[-1].append((h-i-1,j))
                used[h-i-1][j]=1
            if used[h-i-1][w-j-1]==0:
                grid[-1].append((h-i-1,w-j-1))
                used[h-i-1][w-j-1]=1
            if used[i][w-j-1]==0:
                grid[-1].append((i,w-j-1))
                used[i][w-j-1]=1

num=[len(x) for x in grid]
num=sorted(num, reverse=True)
from collections import defaultdict

d=defaultdict(int)
for i in range(h):
    S=list(input())
    for s in S:
        d[s]+=1

for i in range(len(num)):
    for x in range(26):
        if d[chr(97+x)]>=num[i]:
            d[chr(97+x)]-=num[i]
            break

for x in range(26):
    if d[chr(97+x)]>=1:
        print('No')
        exit()
print('Yes')