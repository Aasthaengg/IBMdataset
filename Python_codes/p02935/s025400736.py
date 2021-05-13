from collections import deque
n = int(input())
v = deque(sorted(list(map(int, input().split()))))

while len(v) != 1:
    x = v.popleft()
    y = v.popleft()
    v.appendleft((x+y)/2)
print(v[0])