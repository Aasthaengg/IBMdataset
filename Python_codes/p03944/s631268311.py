w, h, n = map(int,input().split())
left = 0
right = w
up = h
down = 0
for i in range(n):
    x, y, a = map(int,input().split())
    if a==1:
        left = max(left, x)
    elif a==2:
        right = min(right, x)
    elif a==3:
        down = max(down, y)
    else:
        up = min(up, y)
if up-down < 0 and right-left < 0:
    print(0)
else:
    print(max(0,(up-down)*(right-left)))
