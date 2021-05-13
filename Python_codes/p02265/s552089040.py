from sys import stdin
from collections import deque
input = stdin.readline

nodelist = deque()
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == 'insert':
        nodelist.appendleft(command[1])
    elif command[0] == 'delete':
        try:
            nodelist.remove(command[1])
        except:
            continue
    elif command[0] == 'deleteFirst':
        nodelist.popleft()
    else:
        nodelist.pop()
print(*nodelist)
