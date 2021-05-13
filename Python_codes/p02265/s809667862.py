
import sys
from collections import deque

n = int(sys.stdin.readline())
linked_list = deque([])

for i in range(n):
    line = sys.stdin.readline().split()
    cmd = line[0]

    if len(line) == 2:
        value = line[1]

    if cmd == "insert":
        linked_list.appendleft(value)
    elif cmd == "delete":
        if value in linked_list:
            linked_list.remove(value)
    elif cmd == "deleteFirst":
        linked_list.popleft()
    elif cmd == "deleteLast":
        linked_list.pop()

print(*linked_list)