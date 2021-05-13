from collections import deque

def main():

    queue = deque()

    for _ in range(int(input())):
        commands = input().split(" ")
        if commands[0] == "insert":
            queue.appendleft(commands[1])
        elif commands[0] == "delete":
            try:
                queue.remove(commands[1])
            except ValueError:
                pass
        elif commands[0] == "deleteFirst":
            queue.popleft()
        elif commands[0] == "deleteLast":
            queue.pop()

    print(" ".join(queue))

main()