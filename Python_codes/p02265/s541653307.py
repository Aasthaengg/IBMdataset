from collections import deque

n = int(input())
q = deque()
for i in range(n):
    com = input().split()
    if com[0] == 'insert':
        q.appendleft(com[1])
    elif com[0] == 'delete':
        try:
            q.remove(com[1])
        except:
            pass
    elif com[0] == 'deleteFirst':
        q.popleft()
    else:
        q.pop()
print(" ".join(q))
