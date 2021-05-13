from collections import deque
queue = deque([])
n = int(input())
for _ in range(n):
    command = input()
    if command == "deleteFirst":
        _ = queue.popleft()
    elif command == "deleteLast":
        _ = queue.pop()
    elif "delete" in command:
        _, x = command.split()
        try:
            queue.remove(x)
        except ValueError:
            pass
    else:
        _, x = command.split()
        queue.appendleft(x)
print(" ".join(queue))