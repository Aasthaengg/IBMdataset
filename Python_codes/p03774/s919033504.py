n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append([int(i) for i in input().split()])

c = []
for _ in range(m):
    c.append([int(i) for i in input().split()])

for i in range(n):
    ans = 0
    l = 10**16
    for j in range(m):
        tmp = abs(g[i][0] - c[j][0]) + abs(g[i][1] - c[j][1])
        
        if tmp < l:
            l = tmp
            ans = j + 1
            
    print(ans)