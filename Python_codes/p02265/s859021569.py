from collections import deque

DLL = deque()

n = int(input())
for _ in range(n):
    command = input()
    if command == 'deleteFirst':
        DLL.popleft()
    elif command == 'deleteLast':
        DLL.pop()
    else:
        command, x = command.split()
        if command == 'insert':
            DLL.appendleft(x)
        elif command == 'delete':
            try:
                DLL.remove(x)
            except ValueError:
                pass
            
print(' '.join(DLL))
