from collections import deque
S = deque(list(input().strip()))
Q = int(input())
P = 0
for _ in range(Q):
    q = list(input().split())
    if q[0]=="1":
        P += 1
        P = P%2
    else:
        c = q[2]
        if q[1]=="1":
            if P==0:
                S.appendleft(c)
            else:
                S.append(c)
        else:
            if P==0:
                S.append(c)
            else:
                S.appendleft(c)
if P==1:
    S = list(S)
    S = S[::-1]
print("".join(S))