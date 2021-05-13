import queue
n, q = map(int, input().split(" "))
plist = queue.Queue()
for i in range(n):
    plist.put((lambda l: [l[0], int(l[1])])(input().split(" ")))
time = 0
history = queue.Queue()
while not plist.empty():
    p = plist.get()
    if p[1] <= q:
        time += p[1]
        history.put([p[0], time])
    else:
        p[1] -= q
        plist.put(p)
        time += q
while not history.empty():
    p = history.get()
    print("%s %d" % (p[0], p[1]))