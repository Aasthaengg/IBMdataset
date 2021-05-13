n = int(raw_input())
t = 0
h = 0
for i in range(0,n):
    tW,hW, = raw_input().split()
    if tW >hW:
        t += 3
    elif tW == hW:
        t += 1
        h += 1
    else:
        h +=3
print t,h