import sys
from collections import deque

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

ans = []
s = ns()
n = len(s) + 1
now = 0
min_now = 0

ri = deque()
le = deque()

now = 0
for i in range(n-1):
    if s[i] == '<':
        now += 1
    else:
        now = 0
    le.append(now)
now = 0
for i in range(n-1):
    if s[(n-2)-i] == '>':
        now += 1
    else:
        now = 0
    ri.appendleft(now)
le.appendleft(0)
ri.append(0)

for i in range(n):
    ans.append(max(le.popleft(), ri.popleft()))

print(sum(ans))