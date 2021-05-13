from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
Qs = deque()

for i in range(n):
    
    OPs = input().split()
    
    op = OPs[0]
    
    if op[0] == 'i':
        Qs.appendleft(OPs[1])
        continue
    if op == 'delete':
        try:
            Qs.remove(OPs[1])
        except ValueError:
            pass
        continue
    if op == 'deleteFirst':
        Qs.popleft()
        continue
    if op == 'deleteLast':
        Qs.pop()
        continue

print(" ".join(map(str, Qs)))
