n = int(input())
rate = list(map(int, input().split()))
colo = []

for i in rate:
    if 1 <= i < 400:
        if 1 in colo:
            continue
        else:
            colo.append(1)
    if 400 <= i < 800:
        if 2 in colo:
            continue
        else:
            colo.append(2)
    if 800 <= i < 1200:
        if 3 in colo:
            continue
        else:
            colo.append(3)
    if 1200 <= i < 1600:
        if 4 in colo:
            continue
        else:
            colo.append(4)
    if 1600 <= i < 2000:
        if 5 in colo:
            continue
        else:
            colo.append(5)
    if 2000 <= i < 2400:
        if 6 in colo:
            continue
        else:
            colo.append(6)
    if 2400 <= i < 2800:
        if 7 in colo:
            continue
        else:
            colo.append(7)
    if 2800 <= i < 3200:
        if 8 in colo:
            continue
        else:
            colo.append(8)
    if 3200 <= i:
        colo.append(-1)

if -1 not in colo:
    print("{} {}".format(len(colo), len(colo)))
else:
    cnt = 0
    cnt_upto3200 = 0
    for i in range(1, 9):
        if i in colo:
            cnt += 1
    for j in colo:
        if j == -1:
            cnt_upto3200 += 1
    if cnt == 0:
        print("{} {}".format(1,  cnt_upto3200))
    else:
        print("{} {}".format(cnt, cnt + cnt_upto3200))
