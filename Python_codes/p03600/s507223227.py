#074_D
from copy import deepcopy
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

def warshall_floyd(d, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

b = deepcopy(a)
warshall_floyd(b, n)

flg = True
ans = 0
for i in range(n):
    for j in range(n):
        if b[i][j] < a[i][j]:
            flg = False
            break
        else:
            flg2 = True
            for k in range(n):
                if i == k or j == k:
                    continue
                elif b[i][j] == b[i][k] + b[k][j]:
                    flg2 = False
            ans += b[i][j] if flg2 else 0
                    
print(ans//2 if flg else -1)