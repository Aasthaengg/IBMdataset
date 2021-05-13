from collections import deque
S = deque(input())
Q = int(input())
reverse = 0
Tlist = []
for i in range(Q):
    Tlist.append(list(input().split()))
    if Tlist[i][0] == str(2):
        if (int(Tlist[i][1])+reverse) % 2 == 0:
            S.append(Tlist[i][2])
        else:
            S.appendleft(Tlist[i][2])
    else:
        if reverse == 1:
            reverse = 0
        else:
            reverse = 1
if reverse == 0:
    print(''.join(S))
else:
    S.reverse()
    print(''.join(S))
