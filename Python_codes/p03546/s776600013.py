h,w = map(int,input().split())
 
C = []
for i in range(10):
    C.append(list(map(int,input().split())))
 
def warshall_floyd(d):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

trans_map = warshall_floyd(C)
ans = 0
for _ in range(h):
    A = list(map(int,input().split()))
    for a in A:
        if a==-1:
            continue
        else:
            ans += trans_map[a][1]
print(ans)