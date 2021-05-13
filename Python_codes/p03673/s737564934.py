from collections import deque
n=int(input())
a=list(map(int,input().split()))
ans=deque()
rev=False
if n&1:
   rev=True 
for i in a:
    if rev:
        ans.appendleft(i)
    else:
        ans.append(i)
    rev=not rev
print(*ans)