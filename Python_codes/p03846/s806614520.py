import sys
from collections import deque


mod = 10**9 + 7
n = int(input())
a = deque(sorted(list(map(int, (input().split())))))
if n % 2 == 0:
    for i in range(n//2):
        b = a.popleft()
        c = a.popleft()
        if b != i*2+1 or c != i*2+1:
            print(0)
            sys.exit()
    print(pow(2, n//2, mod))

if n % 2 == 1:
    if a.popleft() != 0:
        print(0)
        sys.exit()
    for i in range(n//2):
        b = a.popleft()
        c = a.popleft()
        if b != (i+1)*2 or c != (i+1)*2:
            print(0)
            sys.exit()
    print(pow(2, n//2, mod))