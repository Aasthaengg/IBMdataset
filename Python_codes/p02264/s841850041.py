import queue

n, q = map(int, input().split())
queue = queue.Queue()
for i in range(n):
    name, time = input().split()
    queue.put((name, int(time)))

t = 0
while not queue.empty():
    name, time = queue.get()

    if time <= q:
        t += time
        print(name, t)
    else:
        queue.put((name, time - q))
        t += q

