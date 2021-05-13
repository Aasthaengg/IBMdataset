n, q = [int(a) for a in input().split()]
total_time = 0
queue = []
for i in range(n):
    queue.append([a for a in input().split()])

while len(queue) > 0:
    name = queue[0][0]
    time = int(queue[0][1])
    if time <= q:
        total_time += time
        print(name + " " + str(total_time))
        del queue[0]
    else:
        total_time += q
        time -= q
        queue.append([name, time])
        del queue[0]
