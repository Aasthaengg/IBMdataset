N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
from collections import deque
AA = deque(A)
change = []
for _ in range(M):
    b,c = map(int,input().split())
    change.append((c,b))
change.sort(reverse=True)
import sys
flag = True
for c,b in change:
    for i in range(b):
        a = AA.popleft()
        if a<c:
            AA.append(c)
        else:
            flag = False
            AA.append(a)
            print(sum(AA))
            sys.exit()
if flag:
    print(sum(AA))