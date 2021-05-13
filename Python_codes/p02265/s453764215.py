from collections import deque

N = int(input().rstrip())

dll = deque()

for n in range(N):
    command = input().rstrip()
    if command.endswith(("First", "Last")):
        if command == "deleteFirst":
            dll.popleft()
        else:
            dll.pop()
    else:
        command, x = command.split(" ")
        if command =="insert":
            dll.appendleft(x)
        else:
            try:
                dll.remove(x)
            except Exception as e:
                pass
            
print(" ".join(dll))
