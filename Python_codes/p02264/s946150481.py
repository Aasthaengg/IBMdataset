import queue
q = queue.Queue()
exetime = 0

n, quantum = map(int, input().split())
for i in range(n):
    q.put(tuple(input().split())) # tupleで渡す

while not q.empty():
    process = q.get()
    #print(process)
    time = int(process[1])
    if time > quantum:
        exetime += quantum
        q.put((process[0], time - quantum))
    else:
        exetime += time
        print(process[0], exetime)
