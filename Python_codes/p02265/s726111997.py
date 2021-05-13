from collections import deque
n = int(input())
l = deque()
for i in range(n):
    command = input()
    if command == "deleteFirst":
        l.popleft()
    elif command == "deleteLast":
        l.pop()
    else:
        order, num = command.split()
        if order == "insert":
            l.appendleft(num)
        elif order == "delete":
            try:
                l.remove(num)
            except:
                pass

print(" ".join(l))
