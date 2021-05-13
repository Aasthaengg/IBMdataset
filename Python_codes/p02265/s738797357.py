from collections import deque
n = int(input())
L = deque()
for i in range(n):
    command = input()
    if command == 'deleteFirst':
        L.popleft()
    elif command == 'deleteLast':
        L.pop()
    else:
        c, x = command.split()
        if c == 'insert':
            L.appendleft(x)
        elif c == 'delete':
            try:
                L.remove(x)
            except ValueError:
                pass
print(' '.join(L))
