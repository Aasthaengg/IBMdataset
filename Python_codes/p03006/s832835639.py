n = int(input())
xy = sorted([tuple(map(int,input().split())) for i in range(n)])
if n==1:
    print(1)
    exit()
dif = []
for i in range(n):
    for j in range(i+1,n):
        dif.append(tuple([xy[j][0]-xy[i][0],xy[j][1]-xy[i][1]]))
from collections import Counter
c = Counter(dif)
print(n-max(c.values()))