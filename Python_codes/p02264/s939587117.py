import queue


nq = input().split()
n = int(nq[0])
q = int(nq[1])

qu = queue.Queue()
for _ in range(n):
    nt = input().split()
    qu.put({"name": nt[0], "time": int(nt[1])})

t = 0
while not(qu.empty()):
    process = qu.get()
    if process["time"] > q:
        process["time"] -= q
        t += q
        qu.put(process)
    else:
        t += process["time"]
        print(process["name"], t)
