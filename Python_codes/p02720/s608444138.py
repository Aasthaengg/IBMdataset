import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
K = I()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
queue = deque(A)
cnt = 0
while cnt != (K - 1):
    x = queue.popleft()
    mod = x % 10
    if mod != 0:
        queue.append(10 * x + mod - 1)
    queue.append(10 * x + mod)
    if mod != 9:
        queue.append(10 * x + mod + 1)
    cnt += 1
print(queue.popleft())
