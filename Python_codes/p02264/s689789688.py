import queue
procs = queue.Queue()

n,q = list(map(int,input().split()))

for i in range(n):
    name,time = input().split()
    procs.put((name,int(time)))
time=0
doneprocs = queue.Queue()
while True:
    if procs.empty():
        break
    temp = procs.get()
    if temp[1] <= q:
        time += temp[1]
        doneprocs.put((temp[0],time))
    else:
        time+= q
        procs.put((temp[0],temp[1]-q))
for i in range(n):
    temp = doneprocs.get()
    print(temp[0],temp[1])