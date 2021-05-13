import sys
from copy import deepcopy
N = int(input())
b = [int(i) for i in input().split()]

ans = []
for i, x in enumerate(b):
    if x > i+1:
        print(-1)
        sys.exit()
while len(b) != 0:
    for i, x in enumerate(b[::-1]):
        if len(b)-i == x:
            ans.append(x)
            b.pop(len(b) - i - 1)
            break
print(*ans[::-1], sep='\n')