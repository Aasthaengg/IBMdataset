import queue

n = int(input())
v = [[]]
for _ in range(n):
    edges = sorted([int(x) for x in input().split()][2:])
    v.append(edges)
answers = [[idx, -1] for idx in range(n + 1)]
q = queue.Queue()
q.put(1)

answers[1][1] = 0
while not q.empty():
    node = q.get()
    for next_node in v[node]:
        if answers[next_node][1] != -1:
            continue
        q.put(next_node)
        answers[next_node][1] = answers[node][1] + 1

for idx, time in answers[1:]:
    print(idx, time)

