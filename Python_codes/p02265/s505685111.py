from collections import deque
n = int(input())
dl = deque()
for _ in range(n):
    op = input().split()
    if   op[0] == 'insert'     : dl.appendleft(op[1]) 
    elif op[0] == 'delete'     :
        if op[1] in dl: dl.remove(op[1])
    elif op[0] == 'deleteFirst': dl.popleft() 
    elif op[0] == 'deleteLast' : dl.pop() 
print(*dl)