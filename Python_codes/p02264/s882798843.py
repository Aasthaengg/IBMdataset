n, q = [int(temp) for temp in input().split()]
tim  = 0
dat  = []

for mak in range(n) :
    tem = [temp for temp in input().split()]
    tem[1] = int(tem[1])
    if tem[1] > q :
        tim += q
        dat.append(tem[0])
        dat.append(tem[1] - q)
    else :
        tim += tem[1]
        print(tem[0], tim)

while dat != [] :
    for mak in range(len(dat) // 2) :
        tem = [dat[0], dat[1]]
        if tem[1] > q :
            tim += q
            dat.append(tem[0])
            dat.append(tem[1] - q)
        else :
            tim += tem[1]
            print(tem[0], tim)
        dat.pop(0)
        dat.pop(0)