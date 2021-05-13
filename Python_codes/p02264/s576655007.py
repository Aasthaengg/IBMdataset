# -*- coding:utf-8 -*-

queue = list()
time = 0

n, q = [int(x) for i, x in enumerate(input().split()) if i < 2]
for i in range(n):
    temp = input().split()
    temp[1] = int(temp[1])
    queue.append(temp)
while(len(queue)):
    process = queue.pop(0)
    if process[1] <= q:
        time += process[1]
        print("{0} {1}".format(process[0], time))
    else:
        time += q
        process[1] -= q
        queue.append(process)