N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))
D.sort()
T.sort()
from collections import deque
D = deque(D)
T = deque(T)
while T:
    t = T.popleft()
    flag = False
    while D:
        new = D.popleft()
        if new == t:
            flag = True
            break
    if not flag:
        print('NO')
        exit()
print('YES')
