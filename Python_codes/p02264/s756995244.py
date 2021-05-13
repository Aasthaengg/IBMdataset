import sys
n, q = list(map(int, input().split()))

robin = list(map(lambda y: [y[0], int(y[1])], list(map(lambda x: x.split(), sys.stdin))))

t = []
time = 0
while 0 < len(robin):
    r = robin.pop(0)
    remain = r[1]
    if q < remain:
        r[1] = remain - q
        robin.append(r)
        time += q
    else:
        time += remain
        t.append([r[0], time])

for i in t:
    print(' '.join(map(str, i)))