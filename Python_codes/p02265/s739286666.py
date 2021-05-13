from collections import deque

q = deque()

n = int(input().strip())

for _ in range(n):
    cmd = input()
    if cmd == "deleteFirst":
        q.popleft()
    elif cmd == "deleteLast":
        q.pop()
    elif cmd.startswith("insert "):
        v = cmd[7:]
        q.appendleft(v)
    elif cmd.startswith("delete "):
        v = cmd[7:]
        try:
            q.remove(v)
        except ValueError:
            pass
print(" ".join(q))