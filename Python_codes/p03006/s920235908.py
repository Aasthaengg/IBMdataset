from collections import *

N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

if N==1:
    print(1)
    exit()
    
cnt = defaultdict(int)

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        
        cnt[(xy[i][0]-xy[j][0], xy[i][1]-xy[j][1])] += 1

M = max(list(cnt.values()))
print(N-M)