from collections import deque

queue = deque([])

n = int(input())

for i in range(n):
    commands = input().split(" ")
    command = commands[0]
    if command == "insert":
        queue.appendleft(commands[1])
    elif command == "delete":
        try:
            queue.remove(commands[1])
        except ValueError:
            pass
    elif command == "deleteFirst":
        queue.popleft()
    elif command == "deleteLast":
        queue.pop()

last = queue.pop()
for i in queue:
    print(i, end=" ")

print(last)