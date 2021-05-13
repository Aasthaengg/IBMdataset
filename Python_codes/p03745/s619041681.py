n, *a = map(int, open(0).read().split())

isInc = False
isDec = False
cnt = 1
bef_a = a[0]

for ai in a:
    if isInc and bef_a > ai:
        cnt += 1
        isInc = False
    elif isDec and bef_a < ai:
        cnt += 1
        isDec = False
    elif isInc == False and isDec == False:
        if bef_a < ai:
            isInc = True
        elif bef_a > ai:
            isDec = True
    bef_a = ai
print(cnt)