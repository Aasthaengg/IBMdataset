point = [0,0]
for i in range(int(input())):
    (t,h) = [x for x in input().split()]
    if t == h:
        point[0] += 1
        point[1] += 1
    else:
        a = [t,h]
        q = sorted(a)
        if t == q[0]:
            point[1] += 3
        else:
            point[0] += 3
print(point[0],point[1])