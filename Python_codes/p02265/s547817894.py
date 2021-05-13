from collections import deque
from sys import stdin

n = int(input())

q = deque()

for _ in range(n):
	cmd = stdin.readline().strip().split()
	if cmd[0] == "insert":
		q.appendleft(cmd[1])
	elif cmd[0] == "deleteFirst":
		q.popleft()
	elif cmd[0] == "deleteLast":
		q.pop()
	elif cmd[0] == "delete":
		try:
			q.remove(cmd[1])
		except:
			pass

print(*q)

