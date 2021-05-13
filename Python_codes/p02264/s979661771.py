from Queue import Queue
n, q = map(int, raw_input().split())
P = []
for i in xrange(n):
    x = raw_input().split()
    P.append((x[0], int(x[1])))

Q = Queue()
for x in P:
    Q.put(x)
total = 0
while not Q.empty():
    x = Q.get()
    if x[1] <= q:
        total += x[1]
        print x[0], total
    else:
        total += q
        Q.put((x[0], x[1]-q))