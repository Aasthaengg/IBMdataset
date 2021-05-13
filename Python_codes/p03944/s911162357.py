w,h,n = map(int,input().split())
lists = [list(map(int,input().split())) for i in range(n)]
plx = 0
ply = 0
prx = w
pry = h
for x,y,a in lists:
    if a == 1:
        if plx < x:
            plx = x
    elif a == 2:
        if prx > x:
            prx = x
    elif a == 3:
        if ply < y:
            ply = y
    elif a == 4:
        if pry > y:
            pry = y
px = (prx - plx)
if px < 0:
    px = 0
py = (pry - ply)
if py < 0:
    py = 0
ans = px * py
if ans < 0:
    ans = 0
print(ans)
