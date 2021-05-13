
from collections import defaultdict

N,C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(C)]
change = dict()
for i in range(C):
    for j in range(C):
        change[(i+1,j+1)] = D[i][j]

grid = [tuple(map(int, input().split())) for _ in range(N)]

mod_0 = defaultdict(int)
mod_1 = defaultdict(int)
mod_2 = defaultdict(int)

for i in range(N):
    for j in range(N):
        if (i+1 + j + 1) % 3 == 0:
            mod_0[grid[i][j]] += 1
        elif (i+1 + j + 1) % 3 == 1:
            mod_1[grid[i][j]] += 1
        elif (i+1 + j + 1) % 3 == 2:
            mod_2[grid[i][j]] += 1

ans = float("inf")
# 色のとり方
# 余り0がi,1がj,2がkになる
for i in range(C):
    
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            tmp = 0
            if i == k or j == k:
                continue
            
            for c,v in mod_0.items():
               tmp += change[(c, i+1)] * v
            for c,v in mod_1.items():
                   tmp += change[(c, j+1)] * v
            for c,v in mod_2.items():
                   tmp += change[(c, k+1)] * v

            ans = min(ans, tmp)
            
print(ans)