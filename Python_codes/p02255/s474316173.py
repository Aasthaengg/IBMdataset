length = int(input())
targ = [int(n) for n in input().split(' ')]
for l in range(length):
    insert = 0
    for m in range(l):
        if targ[l] >= targ[l - m - 1]:
            insert = l - m
            break
    aftdisp = targ[l]
    for i in range(0,l - insert):
        disp = targ[l - i]
        targ[l - i] = targ[l - i - 1]
        targ[l - i - 1] = disp
    print(" ".join([str(n) for n in targ]))