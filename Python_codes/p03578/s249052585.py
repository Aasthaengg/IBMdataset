n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d.sort()
t.sort()

from collections import deque

d = deque(d)
t = deque(t)

while len(t) > 0 and len(d) > 0:
	if d[0] == t[0]:
		d.popleft()
		t.popleft()
	else:
		d.popleft()

print('YES') if len(t) == 0 else print('NO')