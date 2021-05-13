from collections import deque
n=int(input())
que=deque()

for i in range(n):
    command=input()
    if command=="deleteFirst":que.popleft()
    elif command=="deleteLast":que.pop()
    else:
        x,y=command.split()
        if x=="insert":que.appendleft(y)
        else:
            if y in que:que.remove(y)

print(*que)
