# E - Red and Green Apples
from collections import deque

X,Y,A,B,C = map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
R = list(map(int,input().split()))
P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)
P = deque(P)
Q = deque(Q)
R = deque(R)
red,green = 0,0
apple = [P.popleft(), Q.popleft(), R.popleft()]
ans = 0

for _ in range(X+Y):
    mapple = max(apple)
    ans += mapple
    if apple[2]==mapple:
        if len(R)>0:
            apple[2] = R.popleft()
        else:
            apple[2] = -1
    elif apple[0]==mapple:
        red += 1
        if red<X:
            apple[0] = P.popleft()
        else:
            apple[0] = -1
    else:
        green += 1
        if green<Y:
            apple[1] = Q.popleft()
        else:
            apple[1] = -1

print(ans)