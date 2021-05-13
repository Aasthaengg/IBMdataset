from collections import deque

N, M = [int(x) for x in input().split()]
route = {int(x): [] for x in range(N)}

for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    route[a].append(b)
    route[b].append(a)

queue = deque()
queue.append(0)

all_town = set([int(x) for x in range(N)])

result = 0
while queue:
    pos = queue.popleft()
    all_town.discard(pos)

    for next_pos in route[pos]:
        if next_pos in all_town:
            queue.append(next_pos)

    if not queue:
        if all_town:
            queue.append(all_town.pop())
            result += 1

print(result)
