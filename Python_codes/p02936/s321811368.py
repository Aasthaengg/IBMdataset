from collections import deque

N, Q = [int(x) for x in input().split()]

tree = {}
result = [0] * N

for _ in range(N-1):
    a, b = [int(x) - 1 for x in input().split()]
    if a in tree:
        tree[a].append(b)
    else:
        tree[a] = [b]

    if b in tree:
        tree[b].append(a)
    else:
        tree[b] = [a]


add = [0] * N
for _ in range(Q):
    p, x = [int(x) for x in input().split()]

    add[p-1] += x

queue = deque()
queue.appendleft((0, add[0]))

finished = set()

while queue:
    target = queue.pop()
    node = target[0]
    count = target[1]

    result[node] = count
    finished.add(node)

    if node in tree:
        for next_node in tree[node]:
            if not next_node in finished:
                queue.appendleft((next_node, count + add[next_node]))

print(" ".join(map(str, result)))
