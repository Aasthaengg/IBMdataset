from collections import deque

N = int(input())
a = list(map(int, input().split()))

d = deque()

for x in range(N):
    if x % 2 == 0:
        d.append(str(a[x]))
    else:
        d.appendleft(str(a[x]))
if N % 2 == 0:
    print(" ".join(d))
else:
    print(" ".join(reversed(d)))
