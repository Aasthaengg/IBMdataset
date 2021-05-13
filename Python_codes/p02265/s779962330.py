from collections import deque

queue = deque([])

for _ in range(int(input())):
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

print(" ".join(queue))