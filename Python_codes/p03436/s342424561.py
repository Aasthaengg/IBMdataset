from collections import deque

Y, X = map(int,input().split())
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
sy,sx = 1,1
gy,gx = Y,X
s = [["#"]*(X+2) for _ in range(Y+2)]
for y in range(Y):
    s[y+1] = list("#"+input()+"#")
inf = Y*X
c = [[inf]*X for _ in range(Y)]
c[sy-1][sx-1] = 0
drs = [(-1,0),(1,0),(0,-1),(0,1)]
q = deque([(sy-1, sx-1)])

while q:
    y,x = q.pop()
    cost = c[y][x]
    for dx,dy in drs:
        x2 = x+dx
        y2 = y+dy
        if s[y2+1][x2+1] == "." and c[y2][x2] > cost+1:
            c[y2][x2] = cost+1
            q.append((y2,x2))
if c[gy-1][gx-1] == inf:
    print("-1")
else:
    dots = 0
    for s1 in s:
        dots +=s1.count(".")
    print(dots-c[gy-1][gx-1]-1)