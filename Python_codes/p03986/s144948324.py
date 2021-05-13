from collections import deque

s = input()
q = deque()

for si in s:
    if si == "S":
        q.append(si)
    elif si == "T" and len(q) == 0:
        q.append(si)
    elif q[-1] == "T":
        q.append(si)
    elif q[-1] == "S":
        q.pop()
print(len(q))