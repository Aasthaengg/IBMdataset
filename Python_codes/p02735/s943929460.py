h , w = map(int,input().split())
p = []
for i in range(h):
    kar = list(input())
    p.append(kar)
d = [[0 for i in range(w)] for j in range(h)]
for i in range(w):
    if i == 0:
        if p[0][0] == "#":
            d[0][0] = 1
    else:
        if p[0][i-1] == "." and p[0][i] == "#":
            d[0][i] += 1
        d[0][i] += d[0][i-1]
for i in range(1,h):
    if p[i-1][0] == "." and p[i][0] == "#":
        d[i][0] += 1
    d[i][0] += d[i-1][0]    

for x in range(1,w):
    for y in range(1,h):
        m = 0
        s = 0
        if p[y][x-1] == "." and p[y][x] == "#":
            m += 1
        m += d[y][x-1]
        if p[y-1][x] == "." and p[y][x] == "#":
            s += 1
        s += d[y-1][x]
        d[y][x] = min(m,s)
print(d[h-1][w-1])