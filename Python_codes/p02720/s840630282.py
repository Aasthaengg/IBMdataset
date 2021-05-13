k = int(input())
from collections import deque
queue = deque([i+1 for i in range(9)])
anses = [i+1 for i in range(9)]
while len(anses) < k:
    now = deque.popleft(queue)
    last = now%10
    if last == 0:
        look = [0, 1]
    elif last == 9:
        look = [8, 9]
    else:
        look = [last-1, last, last+1]
    for i in look:
        anses.append((10*now) + i)
        queue.append((10*now) + i)
print(anses[k-1])