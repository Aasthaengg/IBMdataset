n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int,input().split())))
a,b=xy[0]
m1=a+b
p1=xy[0]
m2=a-b
p2=xy[0]
p3=xy[0]
p4=xy[0]
m3=-a-b
m4=-a+b

for x,y in xy:
    if x+y > m1:
        m1=x+y
        p1 = [x,y]
    if x-y > m2:
        m2=x-y
        p2 = [x,y]
    if -x-y > m3:
        m3 = -x-y
        p3 = [x,y]
    if -x+y > m4:
        m4 = -x+y
        p4 = [x,y]
m = 0
for x0,y0 in [p1,p2,p3,p4]:
    for x1,y1 in [p1,p2,p3,p4]:
        dis=abs(x0-x1) + abs(y0-y1)
        if dis > m:
            m = dis
print(m)