from itertools import combinations
from collections import deque
n,k = map(int,input().split())
i_canerase = [n-2] * n
import sys
q = deque(combinations([i for i in range(n)],2))
use_edges = []
canmake = 0
while q:
    if canmake == k:
        use_edges += list(q)
        print(len(use_edges))
        for i in range(len(use_edges)):
            a,b = use_edges[i]
            print(a+1,b+1)
        sys.exit()

    a,b = q.popleft()
    if i_canerase[a]>0 and i_canerase[b]>0:
        i_canerase[a] -= 1
        i_canerase[b] -= 1
        canmake += 1
    else:
        use_edges.append([a,b])

print(-1)
