dx = [-1,-1,-1,0,0,1,1,1,0]
dy = [-1,0,1,-1,1,-1,0,1,0]
H,W,N = map(int,input().split())
from collections import defaultdict, Counter
d = defaultdict(int)
for i in range(N):
    a,b = map(int,input().split())
    for j in range(9):
        A = a + dy[j]
        B = b + dx[j]
        f = 0
        if 2 <= A <= H-1:
            if 2 <= B <= W-1:
                f = 1
        if f == 1:
            d[(A,B)] += 1
s = 0
c = Counter(d.values())
for i in range(1,10):
    s += c[i]
c[0] = (H-2)*(W-2) - s
for i in range(10):
    print(c[i])