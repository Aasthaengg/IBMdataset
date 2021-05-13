




S = input()
gx, gy = map(int, input().split())


op_x = []
op_y = []
cnt_turn = 0
cnt_f = 0
sx,sy = 0, 0
for s in S:
    if s == "F":
        cnt_f += 1
    else:
        if cnt_turn  == 0:
            sx = cnt_f
            cnt_turn += 1
            cnt_f = 0
        elif cnt_turn % 2 == 0:
            op_x.append(cnt_f)
            cnt_turn += 1
            cnt_f = 0
        else:
            op_y.append(cnt_f)
            cnt_turn += 1
            cnt_f = 0

if cnt_turn  == 0:
    sx = cnt_f
    cnt_turn += 1
    cnt_f = 0
elif cnt_turn % 2 == 0:
    op_x.append(cnt_f)
    cnt_turn += 1
    cnt_f = 0
else:
    op_y.append(cnt_f)
    cnt_turn += 1
    cnt_f = 0

X = set()
X.add(sx)
for dx in op_x:
    nxt = set()
    for x in X:
        nxt.add(x + dx)
        nxt.add(x - dx)
    X = nxt

Y = set()
Y.add(sy)
for dy in op_y:
    nxt = set()
    for y in Y:
        nxt.add(y + dy)
        nxt.add(y - dy)
    Y = nxt

print("Yes" if gx in X and gy in Y else "No")
