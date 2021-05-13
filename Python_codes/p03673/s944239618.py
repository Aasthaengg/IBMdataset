from collections import deque
n=int(input())
A=list(map(int,input().split()))
ans = deque([])
for i in range(n):
  if i % 2 == 0:
    ans.append(A[i])
  else:
    ans.appendleft(A[i])
if n % 2 == 1:
  ans = list(ans)[::-1]
print(*ans)