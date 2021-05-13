N = int(input())
from collections import deque
a = deque(list(map(int, input().split())))
a.append(0)
a.appendleft(0)
s = 0
for i in range(N + 1):
    s += abs(a[i + 1] - a[i]) 
for i in range(1, N + 1):
    ans = s - abs(a[i] - a[i - 1]) - abs(a[i + 1] - a[i]) + abs(a[i + 1] - a[i - 1])
    print(ans)