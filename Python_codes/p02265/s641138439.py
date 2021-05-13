from collections import deque
from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


LIST = deque()

num_command = int(input())

for loop in range(num_command):

    input_command = input()

    if input_command == 'deleteFirst':
        LIST.popleft()
    elif input_command == 'deleteLast':
        LIST.pop();
    else:
        com,num = input_command.split()

        if com == 'insert':
            LIST.appendleft(num)
        elif com == 'delete':
            try:
                LIST.remove(num)
            except:
                pass

print(' '.join(LIST))


