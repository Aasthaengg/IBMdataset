import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
n = int(input())
a = list(map(int,input().split()))
b = deque()

# print(a)
rev = False
for i in a:
    if rev:
        b.appendleft(i)
    else:
        b.append(i)
    rev = not rev

if rev:
    b.reverse()

for i in b:
    print(i)
