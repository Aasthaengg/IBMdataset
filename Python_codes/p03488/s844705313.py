s = input()
n = len(s)
xy = list(map(int, input().split()))

right = 0
updown = []
rightleft = []

direction = 0
for i in range(n):
    if s[i]=='F':
        if direction == 0:
            right+=1
        elif direction == 1:
            updown[-1]+=1
        else:
            rightleft[-1]+=1
    else:
        if direction == 0 or direction == 2:
            direction = 1
            updown.append(0)
        else:
            direction = 2
            rightleft.append(0)

updown = [x for x in updown if x!=0]
rightleft = [x for x in rightleft if x!=0]

# 最初はx方向にしか進めないので補正
xy[0]-=right

# updownでyに行けるか？rightleftでxに行けるかを考えれば良い
dpy = [set() for i in range(len(updown)+1)]
dpy[0].add(0)
for i in range(len(updown)):
    for y in dpy[i]:
        dpy[i+1].add(y+updown[i])
        dpy[i+1].add(y-updown[i])

dpx = [set() for i in range(len(rightleft)+1)]
dpx[0].add(0)
for i in range(len(rightleft)):
    for x in dpx[i]:
        dpx[i+1].add(x+rightleft[i])
        dpx[i+1].add(x-rightleft[i])

if xy[1] in dpy[-1] and xy[0] in dpx[-1]:
    print('Yes')
else:
    print('No')