h,w = map(int,input().split())
x = []
for i in range(h):
    x.append(input())

l = [[0]*w for i in range(h)]
r = [[0]*w for i in range(h)]
u = [[0]*w for i in range(h)]
d = [[0]*w for i in range(h)]

for i in range(h):
    c = 0
    for j in range(w):
        if x[i][j] == '.':
            l[i][j] = c
            c += 1
        else: c=0


for i in range(h):
    c = 0
    for j in range(w):
        if x[i][w-1-j] == '.':
            r[i][w-1-j] = c
            c += 1
        else: c=0

for i in range(w):
    c = 0
    for j in range(h):
        if x[j][i] == '.':
            u[j][i] = c
            c += 1
        else: c=0

for i in range(w):
    c = 0
    for j in range(h):
        if x[h-1-j][i] == '.':
            d[h-1-j][i] = c
            c += 1
        else: c=0

ans = 0
for i in range(h):
    for j in range(w):
        c = l[i][j]+r[i][j]+u[i][j]+d[i][j]
        if x[i][j]=='.':c+=1
        ans = max(ans,c)

print(ans)