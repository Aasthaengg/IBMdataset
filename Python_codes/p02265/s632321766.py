import sys
from collections import deque
readline = sys.stdin.readline
dq = deque()
for _ in range(int(input())):
    c = readline().split()
    if c[0] == "deleteFirst":
        del dq[0]
    elif c[0] == "deleteLast":
        del dq[-1]
    else:
        if c[0] == "insert":
            dq.appendleft(c[1])
        elif c[0] == "delete":
            if c[1] in dq:
                dq.remove(c[1])
print(*dq)

