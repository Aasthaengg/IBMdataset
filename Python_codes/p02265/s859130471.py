from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
d = deque()
for _ in range(n):
    l = input().strip()
    if "deleteFirst" == l:d.popleft();continue
    elif "deleteLast" == l: d.pop();continue
    c, s = l.split()
    if c == "insert": d.appendleft(s);continue
    elif s in d: d.remove(s)
print(*d)
