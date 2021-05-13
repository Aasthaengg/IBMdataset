from itertools import permutations

n,cn = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(cn)]
c = [list(map(int,input().split())) for _ in range(n)]

col_count = [[0] * cn for _ in range(3)]
for i in range(n):
    for j in range(n):
        col_count[(i+j+2)%3][c[i][j]-1] += 1

ans = 1000*n*n
for c123 in permutations(range(cn),3):
    dsum = 0
    for i in range(3):
        for j in range(cn):
            dsum += d[j][c123[i]] * col_count[i][j]
    ans = min(ans,dsum)
print(ans)