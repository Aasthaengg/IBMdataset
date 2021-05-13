from collections import deque 

n=int(input())
l=deque()

for loop in range(n):
    command=input()
    
    if command=='deleteFirst':
        l.popleft()
    elif command=='deleteLast':
        l.pop()
    else:
        com,num=command.split()

        if com=='insert':
            l.appendleft(num)
        elif com=='delete':
            try:l.remove(num)
            except:pass
    
print(*l)
