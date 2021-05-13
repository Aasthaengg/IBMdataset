from collections import deque
que = deque()
for _ in range(int(input())):
    op, v = (input().split() + ["1"])[:2]
    if op == "insert":
        que.appendleft(v)
    elif op == "delete":
        try:
            que.remove(v)
        except:
            pass
    elif op == "deleteFirst":
        que.popleft()
    elif op == "deleteLast":
        que.pop()
print(' '.join(que))     
