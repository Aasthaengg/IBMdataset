n = int(input())
cnt = 0
queue = []
last = {}
for _ in range(n):
    p = int(input())
    if p-1 not in last.keys():
        last[p] = len(queue)
        queue.append([p])
        if cnt < 1:
            cnt = 1
    else:
        queue[last[p-1]].append(p)
        last[p] = last[p-1]
        if cnt < len(queue[last[p-1]]):
            cnt = len(queue[last[p-1]])

print(n-cnt)
