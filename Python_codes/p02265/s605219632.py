from collections import deque
import sys

if __name__ == '__main__':
    n = int(input())
    d = deque()

    for command in sys.stdin.readlines():

        if command.startswith("insert"):
            d.appendleft(int(command[len("insert"):]))
        elif command.startswith("delete "):
            if int(command[len("delete"):]) in d:
                d.remove(int(command[-2]))
        elif command.startswith("deleteLast"):
            d.pop()
        elif command.startswith("deleteFirst"):
            d.popleft()
        else:
            print(command)

        # print(*d, command, e)
    print(*d)
