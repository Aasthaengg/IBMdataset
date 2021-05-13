import sys
sys.setrecursionlimit(10**9)
from collections import deque
K = int(input())
queue = deque([1,2,3,4,5,6,7,8,9])
def rec(queue,i):
    x = queue[i]
    if x >= 3234566667:
        return queue
    r = x % 10
    if (r != 0):
        new_x = x * 10 + (r) - 1
        queue.append(new_x)
    new_x = x * 10 + (r)
    queue.append(new_x)
    if (r != 9):
        new_x = x * 10 + r + 1
        queue.append(new_x)
    return rec(queue,i+1)
res = rec(queue,0)
print(res[K-1])