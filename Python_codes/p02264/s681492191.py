n, q = map(int, input().split())

queue = []

for i in range(n):
    name, time = map(str, input().split())
    queue.append([name, int(time)])

time = 0

while len(queue) != 0:
    p = queue.pop(0)
    if p[1] <= q:
        time += p[1]
        print(p[0], time)
    else:
        time += q
        p[1] -= q
        queue.append(p)

