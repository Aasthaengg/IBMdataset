from collections import deque

n = int(input())
data = deque()

for i in range(n):
	command = input().split()
	if len(command) == 2:
		command,x = command
	else:
		command = command[0]
	if command == 'insert':
		data.appendleft(x)
	elif command == 'delete':
		if x in data:
			data.remove(x)
	elif command == 'deleteFirst':
		data.popleft()
	elif command == 'deleteLast':
		data.pop()

print(*data)