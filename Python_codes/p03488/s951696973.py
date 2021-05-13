s = input()
x,y = map(int,input().split())
wayx = []
wayy = []
pad = 15000
can_reachx = [False for i in range(pad*2+1)]
can_reachy = [False for i in range(pad*2+1)]


state = True
seq = 0
for c in s:
    if c == "T":
        if state:
            wayx.append(seq)
            seq = 0
            state = False
        else:
            wayy.append(seq)
            seq = 0
            state = True
    else:
        seq += 1


if state:
    wayx.append(seq)
    seq = 0
    state = False
else:
    wayy.append(seq)
    seq = 0
    state = True

can_reachx[pad+wayx[0]] = True
can_reachy[pad] = True

for i in range(1,len(wayx)):
    w = wayx[i]
    b = []
    for j in range(len(can_reachx)):
        if can_reachx[j]:
            if j+w <= pad*2:
                b.append(j+w)
            if j-w >= 0:
                b.append(j-w)
            can_reachx[j] = False
    for t in b:
        can_reachx[t] = True

for w in wayy:
    b = []
    for i in range(len(can_reachy)):
        if can_reachy[i]:
            if i+w <= pad*2:
                b.append(i+w)
            if i-w >= 0:
                b.append(i-w)
            can_reachy[i] = False
    for t in b:
        can_reachy[t] = True

if can_reachx[x+pad] and can_reachy[y+pad]:
    print("Yes")
else:
    print("No")
