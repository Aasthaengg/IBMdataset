n, q = map(int, input().split())
queue = []
for i in range(n):
    x = input().split()
    queue.append((x[0], int(x[1])))
time = 0
while queue != []:
    if queue[0][1] <= q:
        time += queue[0][1]
        print('{} {}'.format(queue.pop(0)[0], time))
    else:
        time += q
        x = queue.pop(0)
        queue.append((x[0], x[1]-q))
