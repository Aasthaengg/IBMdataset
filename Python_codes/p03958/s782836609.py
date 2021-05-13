k, t = map(int, input().split())
dat = list(map(int, input().split()))
dat.sort(reverse=True)
prev = -1
res = 0
eat = 0
if len(dat) == 1:
    print(dat[0] - 1)
else:
    dat.sort(reverse=True)
    while dat[1] != 0:
        x = dat[1]
        dat[0] -= x
        dat[1] = 0
        dat.sort(reverse=True)
    if dat[0] == 0:
        print(0)
    else:
        print(dat[0] - 1)
