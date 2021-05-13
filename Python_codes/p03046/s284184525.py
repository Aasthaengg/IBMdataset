n, k = map(int, raw_input().strip().split())

if k == 0:
    sz = 1 << n
    sz -= 1
    out = [' '.join([str(i), str(i)]) for i in xrange(sz + 1)]
    print ' '.join(out)
    exit()

m = 1 << n
if k >= m:
    print -1
    exit()

if n < 2:
    print -1
    exit()

l = []
for i in xrange(m):
    if i == k: continue
    l.append(i)

l.append(k)
for i in xrange(m - 1, -1, -1):
    if i == k: continue
    l.append(i)
l.append(k)

print ' '.join(map(str, l))