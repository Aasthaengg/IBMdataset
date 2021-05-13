# encoding: utf-8

n, q = map(int, raw_input().split())
queue = []
for i in xrange(n):
    name, time = raw_input().split()
    queue.append((name, int(time)))

time = 0
while queue:
    name, t = queue.pop(0)
    if q < t:
        time += q
        queue.append((name, t - q))
    else:
        time += t
        print name, time