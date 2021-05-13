import itertools
from collections import Counter

n,a,b,c = map(int,input().split())
l = [int(input()) for _ in range(n)]
le = [i for i in range(4)]

bb = list(itertools.product(le, repeat=n))
new = []
ans = 1145141919810

for ll in bb:
    aa = 0
    con = [0]*4
    amo = [0]*4
    for i in range(n):
        con[ll[i]] += l[i]
        amo[ll[i]] += 1
        
    if con[1] > 0 and con[2] > 0 and con[3] > 0:
        for j in range(1,4):
            aa += (amo[j] - 1) * 10
        aa += abs(con[1] - a)
        aa += abs(con[2] - b)
        aa += abs(con[3] - c)
        
        ans = min(ans,aa)
        
    else:
        continue
        
print(ans)