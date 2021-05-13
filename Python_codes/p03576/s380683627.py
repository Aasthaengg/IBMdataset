import itertools

n,k = map(int, input().split())
z = [list(map(int, input().split())) for i in range(n)]

a = [i for i in range(n)]
c = list(itertools.combinations(a,2))
ans = float('inf')


for x in c:
    for y in c:
        d = 0
        x1 = max(z[x[0]][0],z[x[1]][0])
        x2 = min(z[x[0]][0],z[x[1]][0])
        y1 = max(z[y[0]][1],z[y[1]][1])
        y2 = min(z[y[0]][1],z[y[1]][1])
        for i in range(n):
            if x2 <= z[i][0] <= x1 and y2 <= z[i][1] <= y1:
                d += 1
        if d == k:
            ans = min(ans, (x1-x2)*(y1-y2))

print(ans)