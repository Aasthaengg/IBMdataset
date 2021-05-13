N = int(input())
co = [[int(i) for i in input().split()] for i in range(N)]
co = sorted(co)
d = {}
m = 0
for i in range(N):
    for j in range(i+1, N):
        a = co[i][0]-co[j][0]
        b = co[i][1]-co[j][1]
        if (a, b) in d:
            d[a,b] += 1
        else:
            d[a,b] = 1
for k in d.values():
    m = max(m, k)
print(N-m)