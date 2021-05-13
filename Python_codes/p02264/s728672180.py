from queue import Queue
n,q = map(int,input().split())
qe = Queue()
current = 0
for i in range(n):
    name, time = input().split()
    time = int(time)
    qe.put((name, time))

while not qe.empty():
    item = qe.get()
    if item is None:
        break
    name, time = item
    c = min(q, time)
    current += c
    time -= c
    if time > 0:
        qe.put((name, time))
    else:
        print(name + ' ' + str(current))