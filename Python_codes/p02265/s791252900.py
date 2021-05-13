from collections import deque

n = int(input())
cmdlst = [input() for cmd in range(n)]
lst = deque()

for cmd in cmdlst:
    if cmd == 'deleteFirst':
        lst.popleft()
    elif cmd == 'deleteLast':
        lst.pop()
    else:
        cmd,x = cmd.split()
        if cmd == 'insert':
            lst.appendleft(x)
        else:
            try:
                lst.remove(x)
            except:
                pass
print(*lst)
