# coding=utf-8

n, q = map(int, input().split())
queue = []
total_time = 0
finished_loop = 0

for i in range(n):
    name, time = input().split()
    queue.append([name, int(time)])

while True:
    n -= finished_loop
    finished_loop = 0
    for i in range(n):
        poped = queue.pop(0)
        name = poped[0]
        time = poped[1]
        if time > q:
            queue.append([name, time - q])
            total_time += q
        else:
            total_time += time
            print(name, total_time)
            finished_loop += 1

    if n == 0:
        break