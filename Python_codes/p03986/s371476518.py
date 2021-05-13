import sys
from collections import deque

X = list(sys.stdin.readline().strip())

s = []
q = deque(X)
while q:
    char = q.popleft()
    if len(s) == 0:
        s.append(char)
        continue
        
    if char == "T" and s[-1] == "S":
        s.pop()

    else:
        s.append(char)

print(len(s))