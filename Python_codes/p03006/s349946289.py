n = int(input())
xyl = []
for _ in range(n):
    x,y = map(int,input().split())
    xyl.append((x,y))

ans = n
set_cover = []
for i in range(n):
    for j in range(i+1, n):
        p = xyl[j][0] - xyl[i][0]
        q = xyl[j][1] - xyl[i][1]
        tmp = n
        for k in range(n):
            for l in range(n):
                x = xyl[l][0] - xyl[k][0]
                y = xyl[l][1] - xyl[k][1]
                if p == x and q == y:
                    tmp -= 1
        ans = min(ans, tmp)
print(ans)
