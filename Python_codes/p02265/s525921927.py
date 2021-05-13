import sys
from collections import deque
n = int(sys.stdin.readline())
lines = sys.stdin.readlines()

Q = deque()
for i in range(n):
    command = lines[i].split()
    if command[0] == 'insert':
        Q.appendleft(command[1])
    elif command[0] == 'delete':
        try:
            Q.remove(command[1])
        except:
            pass
    elif command[0] == 'deleteFirst':
        Q.popleft()
    elif command[0] == 'deleteLast':
        Q.pop()
print(' '.join(Q))