import math
n,d = map(int,input().split())
xy = [list(map(int,input().split())) for i in range(n)]

ans = 0
for i in range(n):
    x = xy[i][0] ** 2
    y = xy[i][1] ** 2
    sub = math.sqrt(x+y)
    if sub <= d:
        ans += 1
        
print(ans)        