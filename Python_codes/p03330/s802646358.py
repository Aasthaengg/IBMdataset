import sys
input = sys.stdin.readline
from collections import *

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]
cnt = defaultdict(lambda: defaultdict(int))

for i in range(N):
    for j in range(N):
        cnt[(i+j)%3][c[i][j]-1] += 1

ans = 10**18

for c1 in range(C):
    for c2 in range(C):
        for c3 in range(C):
            if c1==c2 or c2==c3 or c3==c1:
                continue
            
            cand = 0
            
            for k, v in cnt[0].items():
                cand += v*D[k][c1]
            
            for k, v in cnt[1].items():
                cand += v*D[k][c2]
            
            for k, v in cnt[2].items():
                cand += v*D[k][c3]
            
            ans = min(ans, cand)

print(ans)