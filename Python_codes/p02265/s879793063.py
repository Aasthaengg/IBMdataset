from collections import deque
n = int(input())
dl = deque()
for _ in range(n):
    cmd = input()
    if ' ' in cmd:
        op,v = cmd.split()
    else:
        op = cmd
    if   op == 'insert'     : dl.appendleft(v) 
    elif op == 'delete'     :
        try: dl.remove(v)
        except ValueError: pass
    elif op == 'deleteFirst': dl.popleft() 
    elif op == 'deleteLast' : dl.pop() 
print(*dl)