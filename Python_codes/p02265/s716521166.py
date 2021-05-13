from collections import deque
n = int(raw_input())
stack = deque()
for i in range(n):
	i = raw_input()
	if "insert" in i:
		stack.appendleft(int(i[7:]))
	elif "delete " in i:
		if int(i[7:]) in stack:
		    stack.remove(int(i[7:]))
	elif "deleteFirst" in i:
		stack.popleft()
	elif "deleteLast" in i:
		stack.pop()
print " ".join(map(str, stack))