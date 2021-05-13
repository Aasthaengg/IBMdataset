from collections import deque
n=int(input())
dq=deque()

for i in range(n):
    cmd=input().split()
    if cmd[0]=="insert":
        dq.appendleft(cmd[1])
    elif cmd[0]=="deleteFirst":
        dq.popleft()
    elif cmd[0]=="deleteLast":
        dq.pop()
    elif cmd[0]=="delete":
        try:
            dq.remove(cmd[1])
        except:
            pass
print(*dq)