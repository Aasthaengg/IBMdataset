from collections import deque
n = int(input())
v = sorted(map(float, input().split()))
ans = 0
v = deque(v)
while(len(v) > 1):
    v.appendleft(((v.popleft() + v.popleft()) / 2))
print(v[0])