from collections import deque

n = int(input())
d = deque()
for i in range(n):
    tmp = input().split()
    ope = tmp[0]
    if ope == "insert":
        m = tmp[1]
        d.appendleft(m)
    elif ope == "delete":
        m = tmp[1]
        if m in d:
            d.remove(m)
    elif ope == "deleteFirst":
        d.popleft()
    elif ope == "deleteLast":
        d.pop()
print(*d)