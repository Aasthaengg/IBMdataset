import sys
from copy import deepcopy
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
lst1 = [list(map(int,readline().split())) for i in range(n)]

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
st = deepcopy(lst1)
st = warshall_floyd(st)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if lst1[i][j] > st[i][j]:
            print(-1)
            exit()
        elif lst1[i][j]==st[i][j]:
            #他に最短距離がある場合はcontinue
            res = [0]*n
            for k in range(n):
                res[k] += lst1[i][k] + lst1[j][k]
            res[i] = -1
            res[j] = -1
            if any([res[k]==lst1[i][j] for k in range(n)]):
                continue
            else:
                ans += lst1[i][j]
        else:
            ans += lst1[i][j]

print(ans)