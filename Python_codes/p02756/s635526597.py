
from collections import deque

S = input()
Q = int(input())
q = deque(list(S))
rev = 0
for _ in range(Q):
    s, *x = input().split()
    if s == "1":
        rev += 1
    else:
        if ((x[0] == "1" and rev % 2 == 0)
                or (x[0] == "2" and rev % 2 == 1)):
            q.appendleft(x[1])
        else:
            q.append(x[1])

if rev % 2 == 0:
    print("".join(q))
else:
    print("".join(q)[::-1])
