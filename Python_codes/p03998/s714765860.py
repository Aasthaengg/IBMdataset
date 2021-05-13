from collections import deque
SA=deque(input())
SB=deque(input())
SC=deque(input())

ans=""
turn="a"
for i in range(500):
    if turn=="a":
        if len(SA)<1:
            ans="A"
            break
        else:
            turn=SA.popleft()
    elif turn=="b":
        if len(SB)<1:
            ans="B"
            break
        else:
            turn=SB.popleft()
    else:
        if len(SC)<1:
            ans="C"
            break
        else:
            turn=SC.popleft()
    
print(ans)