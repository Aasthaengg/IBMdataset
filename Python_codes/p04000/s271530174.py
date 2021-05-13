import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

H,W,N = MI()

from collections import defaultdict,Counter

d = defaultdict(int)  # d[(i,j)] = [i,i+2]×[j,j+2] に黒いマスが何個あるか
for i in range(N):
    a,b = MI()
    for j in range(max(1,a-2),min(a,H-2)+1):
        for k in range(max(1,b-2),min(b,W-2)+1):
            d[(j,k)] += 1

c = Counter(list(d.values()))
print((H-2)*(W-2)-sum(c.values()))
for i in range(1,10):
    print(c[i])
