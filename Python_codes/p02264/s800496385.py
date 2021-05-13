import sys
import collections

(n, quantum) = map(int, input().split())
processes = [input().split() for i in range(n)]
for p in processes:
    p[1] = int(p[1])
queue = collections.deque(processes)
elapsed = 0
while queue:
    head = queue.popleft()
    if head[1] > quantum:
        head[1] -= quantum
        queue.append(head)
        elapsed += quantum
    else:
        elapsed += head[1]
        print(head[0], elapsed)