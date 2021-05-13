def warshall_floyd(d):
    global n
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

h,w = map(int,input().split())
n = 10
d = [[] for i in range(10)]
for i in range(10):
    for j in map(int,input().split()):
        d[i].append(j)
D = warshall_floyd(d)
ans = 0
for i in range(h):
    for j in map(int,input().split()):
        if j != -1:
            ans += D[j][1]
print(ans)