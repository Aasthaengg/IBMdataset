h,w = map(int,input().split())
c = [[] for i in range(h)]
d = [[1]*w for _ in range(h)]
e = [[1]*w for _ in range(h)]
for i in range(h):
    c[i] = input()
    if c[i][0] == "#":
        d[i][0] = 0
for i in range(w):
    if c[0][i] == "#":
        e[0][i] = 0
    
for i in range(h):
    for j in range(w-1):
        if c[i][j+1] == "#":
            d[i][j+1] = 0
        else:
            d[i][j+1] = d[i][j] + 1
            
for i in range(h-1):
    for j in range(w):
        if c[i+1][j] == "#":
            e[i+1][j] = 0
        else:
            e[i+1][j] = e[i][j] + 1
            
for i in range(h):
    for j in range(w-2,-1,-1):
        if d[i][j] != 0 and d[i][j+1] != 0:
            d[i][j] = d[i][j+1]
        elif d[i][j] != 0 and d[i][j+1] == 0:
            continue
        else:
            d[i][j] = 0
            
for i in range(h-2,-1,-1):
    for j in range(w):
        if e[i][j] != 0 and e[i+1][j] != 0:
            e[i][j] = e[i+1][j]
        elif e[i][j] != 0 and e[i+1][j] == 0:
            continue
        else:
            e[i][j] = 0
            
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans , d[i][j]+e[i][j])
        
print(ans-1)