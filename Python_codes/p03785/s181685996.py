# AGC011 A Airport Bus
import bisect
from collections import deque

n, c, k = map(int, input().split())
t_list = [int(input()) for _ in range(n)]

t_list.sort()
t_list = deque(t_list)
ans = 0

while len(t_list) > 0:
    _tmp = t_list.popleft() + k
    _idx = bisect.bisect_right(t_list, _tmp)
    if c-1 <= _idx:
        for _ in range(c-1):
            t_list.popleft()
    else:
        for _ in range(_idx):
            t_list.popleft()
    ans += 1

print(ans)