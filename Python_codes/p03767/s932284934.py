from collections import deque

N=int(input())
A=list(map(int,input().split()))

A.sort()
B=deque(A)

U=0
while B:
    _=B.popleft()
    _=B.pop()
    x=B.pop()
    U+=x

print(U)
