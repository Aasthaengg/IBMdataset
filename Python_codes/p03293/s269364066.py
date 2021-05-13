from collections import deque
import sys

deque_s = deque(list(input()))
deque_t = deque(list(input()))

for _i in range(len(deque_s)):
    deque_s.rotate()
    if deque_s == deque_t:
        print('Yes')
        sys.exit()

print('No')