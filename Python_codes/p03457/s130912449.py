n = int(input())
t_ = 0
xy_ = [0,0]
for _ in range(n):
    t, *xy = map(int, input().split())
    ta = t - t_
    xya = [abs(xy[0]-xy_[0]), abs(xy[1]-xy_[1])]
    if sum(xya) > ta or (ta - sum(xya))%2 != 0:
        print("No")
        break
    t_ = t
    xy_ = xy
else:
    print("Yes")