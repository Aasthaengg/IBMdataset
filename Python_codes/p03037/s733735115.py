n,m = map(int,input().split())

l = [list(map(int,input().split())) for i in range(m)]

max_l = -1*float('INF')
min_r = float('INF')
for i in range(m):
    max_l = max(max_l,l[i][0])
    min_r = min(min_r,l[i][1])

ans = min_r - max_l + 1

if(ans < 0):
    print(0)
    exit()

if(ans <= n):
    print(ans)
else:
    print(n)
