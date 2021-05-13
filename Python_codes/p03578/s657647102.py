N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

D = sorted(D)
T = sorted(T)

from collections import deque
D = deque(D)
T = deque(T)

if N < M:
    print('NO')
else:
    t = T.popleft()
    for d in D:
#        print(t, d)
        if d == t:
#            print('hit')
            if len(T) == 0:
                print('YES')
                break
            else:
                t = T.popleft()
    else:
        print('NO')