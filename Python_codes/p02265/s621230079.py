from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    tmp = input().split()
    cmd = tmp[0]
    if cmd == 'insert':
        queue.appendleft(tmp[1])
    elif cmd == 'delete':
        try:
            queue.remove(tmp[1])
        except ValueError:
            pass
    elif cmd == 'deleteFirst':
        queue.popleft()
    else:
        queue.pop()

print(' '.join(queue))

