from collections import defaultdict
v_num = int(input())
connect = defaultdict(list)
for v in range(v_num):
    inp = [int(n) - 1 for n in input().split(" ")]
    connect[inp[0]].extend(inp[2:])
answer = [[m + 1, -1] for m in range(v_num)]
queue = [0]
visited = [0 for n in range(v_num)]
visited[0] = 1
time = 0
while queue:
    new_queue = []
    for q in queue:
        answer[q][1] = time
        for c in connect[q]:
            if not visited[c]:
                visited[c] = 1
                new_queue.append(c)
    queue = new_queue
    time += 1
for v in range(v_num):
    print(*answer[v])