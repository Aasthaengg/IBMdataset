


S = input()
X,Y = map(int, input().split())

cnt_T = 0
cnt = 0

step_X = []
step_Y = []
sx = 0
sy = 0
for s in S:
    if s == "F":
        cnt += 1
    else:
        if cnt_T == 0:
            sx = cnt
            cnt = 0
            cnt_T += 1
        elif cnt_T % 2 == 0:
            step_X.append(cnt)
            cnt = 0
            cnt_T += 1
        else:
            step_Y.append(cnt)
            cnt = 0
            cnt_T += 1



if cnt_T == 0:
    sx = cnt
    cnt = 0
    cnt_T += 1
elif cnt_T % 2 == 0:
    step_X.append(cnt)
    cnt = 0
    cnt_T += 1
else:
    step_Y.append(cnt)
    cnt = 0
    cnt_T += 1


dp_X = set()
dp_X.add(sx)
for i in step_X:
    tmp = set()
    for x in dp_X:
        tmp.add(x + i)
        tmp.add(x - i)
    dp_X = tmp

dp_Y = set()
dp_Y.add(sy)
for i in step_Y:
    tmp = set()
    for y in dp_Y:
        tmp.add(y + i)
        tmp.add(y - i)
    dp_Y = tmp

if X in dp_X and Y in dp_Y:
    print("Yes")
else:
    print("No")

