from collections import deque

l = deque([])
n = int(input())
for i in range(n):
    com = input()
    if com == "deleteFirst":
        a = l.popleft()
    elif com == "deleteLast":
        a = l.pop()
    else:
        m = com.split()
        if m[0] == "insert":
            l.appendleft(m[1])
        else:
            try:
                l.remove(m[1])
            except:
                a = 1
print(" ".join(l))