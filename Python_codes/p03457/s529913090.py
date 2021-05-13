n = int(input())
can = True
t,x,y = 0,0,0

for i in range(n):
    t_,x_,y_ = map(int,input().split())
    dt = t_ - t
    dist = abs(x-x_) + abs(y-y_)
    if dt < dist:
        can = False
    else:
        if (dist-dt) % 2 != 0:
            can = False
    t,x,y = t_,x_,y_

print("Yes" if can else "No")