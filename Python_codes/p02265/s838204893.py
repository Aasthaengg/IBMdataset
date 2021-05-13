import sys
from collections import deque


def main():
    line = sys.stdin.readlines()
    deq = deque()
    for i in range(1, int(line[0]) + 1):
        input_command = line[i]

        if input_command[0] == 'i':         # 'insert index'
            deq.appendleft(input_command[7:-1])
        elif input_command[0] == 'd':
            if input_command[6] == ' ':     # 'delete index'
                key = input_command[7:-1]
                if key in deq:
                    deq.remove(key)
            elif input_command[6] == 'F':   # 'deleteFirst':
                deq.popleft()
            elif input_command[6] == 'L':   # 'deleteLast':
                deq.pop()

    print(' '.join(deq))
    return


main()
