from collections import deque
dq = deque()
for mak in range(int(input())) :
    com = input().split()
    if   com[0] == 'insert'      : dq.appendleft(com[1])
    elif com[0] == 'deleteFirst' : dq.popleft()
    elif com[0] == 'deleteLast'  : dq.pop()
    else : 
        if com[1] in dq :
            dq.remove(com[1])
print(' '.join(dq))