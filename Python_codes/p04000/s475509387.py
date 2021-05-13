H, W, N = input().split(" ")
H, W, N = int(H), int(W), int(N)
A = []
for i in range(N):
    A.append([int(j) for j in input().split(" ")])


import itertools
from collections import defaultdict, Counter

c = defaultdict(int)
for a, b in A:
    # そのセルを含む正方形の中心を記録
    for dx,dy in itertools.product([-1,0,1],repeat = 2):
        aa = a + dx
        bb = b + dy
        if 2 <= aa <= H-1 and 2 <= bb <= W-1:
            c[(aa,bb)] += 1
            
result = Counter(c.values())
result[0] = (H-2)*(W-2) - sum(result.values())
 
for j in range(10):
    print(result[j])