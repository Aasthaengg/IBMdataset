from collections import deque
n=int(input())
A=deque()
B=deque()
ans=0
for i in range(n):
    a,b=map(int,input().split())
    A.appendleft(a)
    B.appendleft(b)
while A:
    A[0]+=ans
    if A[0]%B[0]!=0:
        k=B[0]-(A[0]%B[0])
        ans+=k
    A.popleft()
    B.popleft()

print(ans)