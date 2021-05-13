from collections import deque
N = int(input())
de = deque()
for n in range(N):
    com = input().split()
    if com[0] == "insert":
        de.appendleft(com[1])
    elif com[0] == "delete":
        try:
            de.remove(com[1])
        except:
            pass
    elif com[0] == "deleteFirst":
        de.popleft()
    else:
        de.pop()
print(*de)
    
    

