from collections import deque

dq = deque()
n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "insert":
        dq.appendleft(cmd[1])
    elif cmd[0] == "delete":
        try:
            dq.remove(cmd[1])
        except ValueError:
            pass
    elif cmd[0] == "deleteFirst":
        dq.popleft()
    else:
        dq.pop()
print(*dq)