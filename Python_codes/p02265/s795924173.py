import sys
from collections import deque

n = int(input())
que = deque()

for i in range(n):
    command = sys.stdin.readline()[:-1]
    if command[0] == "i":
        que.appendleft(command[7:])
    elif command[6] == " ":
        try:
            que.remove(command[7:])
        except:
            pass
    elif command[6] == "F":
        que.popleft()
    else:
        que.pop()
print(*que)