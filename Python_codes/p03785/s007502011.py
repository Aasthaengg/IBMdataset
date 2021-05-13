from collections import deque
N,C,K = map(int,input().split())
T = []
for i in range(N):
    T.append(int(input()))
T.sort()
T = deque(T)
bus = 0
while True:
    bus += 1
    Time = T[0]+K
    num = 0
    while num < C and T[0] <= Time:
        T.popleft()
        num += 1
        if not T:
            print(bus)
            exit()
