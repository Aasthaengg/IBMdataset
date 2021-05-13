H,W,M = map(int, input().split())
mx=[0] * W
my=[0] * H
bs ={}
mxx = 0
myy = 0
for i in range(M):
    y,x = map(int, input().split())
    mx[x-1] += 1
    my[y-1] += 1
    mxx = max(mx[x-1], mxx)
    myy = max(my[y-1], myy)
    if y-1 in bs:
        bs[y-1].add(x-1)
    else:
        bs[y-1] = set([x-1])

vx = []
vy = []
for i,x in enumerate(mx):
    if x == mxx:
        vx.append(i)
for i,y in enumerate(my):
    if y == myy:
        vy.append(i)

a = 1

for i in vx:
    for j in vy:
        if i not in bs[j]:
            a = 0
            break
    else:
        continue
    break

ans = mxx + myy - a
print(ans)
