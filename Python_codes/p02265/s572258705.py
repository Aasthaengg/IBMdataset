from collections import deque

n = int(input())

linked_list = deque([])

for _ in range(n):
    command = input()

    if "insert" in command:
        x = command.split()[-1]
        linked_list.appendleft(x)
    elif command == "deleteFirst":
        linked_list.popleft()
    elif command == "deleteLast":
        linked_list.pop()
    elif "delete" in command:
        x = command.split()[-1]
        if x in linked_list:
            linked_list.remove(x)

print(*linked_list)

