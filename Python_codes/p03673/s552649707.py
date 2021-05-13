import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

from collections import deque
Q = deque()
for i, a in enumerate(As):
    if i%2==0:
        Q.append(a)
    else:
        Q.appendleft(a)

if N%2==0:
    print(*Q)
else:
    print(*list(Q)[::-1])