from collections import deque
N=int(input())
A=list(map(int,input().split()))

A.sort(reverse=True)
Aq=deque(A)

ans=Aq.popleft()
a=0
for i in range(1,N):
    if i%2==0:
        a=Aq.popleft()
    ans+=a

print(ans)