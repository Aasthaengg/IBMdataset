n = int(input())
A = list(map(int,input().split()))

from collections import deque

d = deque()

for i,a in enumerate(A):
    if i % 2 == 0:
        d.append(a)
    else:
        d.appendleft(a)

if n % 2 != 0:
    d.reverse()

for i in d:
    print(i,end=" ")
print()