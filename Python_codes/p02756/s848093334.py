from collections import deque
S=deque(input())
Q=int(input())
count = 0
for i in range(Q):
    q = list(input().split())
    #print(q)
    if q[0] == "1":
        count += 1
    else:
        if count%2 == 0:
            if q[1] == "1":
                S.appendleft(q[2])
            else:
                S.append(q[2])
        else:
            if q[1] == "1":
                S.append(q[2])
            else:
                S.appendleft(q[2])
if count%2 != 0:
    S = reversed(S)
print("".join(S))
