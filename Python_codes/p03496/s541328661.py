n = input()
num = map(int, raw_input().split())
ma = max(num)
mi = min(num)
l = list()
if ma*mi < 0:
    if ma > abs(mi):
        index = num.index(ma)
    else:
        index = num.index(mi)
    for i in xrange(n):
        l.append("%d %d" % (index+1, i+1))
    b = num[index]
else:
    b = 0
    for i in num:
        if i:
            b = i
            break

if b == 0:
    pass
elif b < 0:
    for i in xrange(n-1, 0, -1):
        l.append("%d %d" % (i+1, i))
else:
    for i in xrange(0, n-1):
        l.append("%d %d" % (i+1, i+2))

print len(l)
for i in l:
    print i
