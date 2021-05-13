from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
lst=[i for i in input().split()]
q=deque([])
for i in range(n):
    if n%2==1:
        if i%2==0:
            q.appendleft(lst[i])
        else:
            q.append(lst[i])
    else:
        if i%2==0:
            q.append(lst[i])
        else:
            q.appendleft(lst[i])

print(" ".join(q))