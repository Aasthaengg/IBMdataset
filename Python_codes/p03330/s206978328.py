n,C = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(C)]
c = [list(map(int,input().split())) for _ in range(n)]

num = []
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        else:
            for k in range(C):
                if i == k or j == k:
                    continue
                else:
                    num.append((i,j,k))
                    
col = [[0]*C for _ in range(3)]

for i in range(n):
    for j in range(n):
        x = c[i][j]-1
        y = (i+j) % 3
        
        col[y][x] += 1
    
ans = 1145141919810
for ll in num:
    a = 0
    for i in range(3):
        for j in range(C):
            a += col[i][j] * d[j][ll[i]]
            
    ans = min(ans,a)
    
print(ans)