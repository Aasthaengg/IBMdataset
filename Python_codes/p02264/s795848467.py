n, q = [int(i) for i in input().split(" ")]

current = 0
queue = []
for _ in range(n):
    name, t = input().split(" ")
    t = int(t)
    if t <= q:
        current += t
        print("{} {}".format(name, current))
    else:
        current += q
        queue.append((name, int(t - q)))

while len(queue) > 0:
    nqueue = []
    for name, t in queue:
        if t <= q:
            t = int(t)
            current += t
            print("{} {}".format(name, current))
        else:
            current += q
            nqueue.append((name, int(t - q)))
    queue = nqueue