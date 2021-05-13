from collections import deque

dq = deque()

n = int(input())

for _ in range(n):
    command = input()
    if command[:6] == 'insert':
        dq.appendleft(command[7:])
    elif command[:10] == 'deleteLast':
        dq.pop()
    elif command[:11] == 'deleteFirst':
        dq.popleft()
    elif command[:6] == 'delete':
        if (command[7:]) in dq:
            dq.remove(command[7:])
print(" ".join(dq))


