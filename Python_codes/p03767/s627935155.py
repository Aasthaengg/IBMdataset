from collections import deque
n = int(input())

a = tuple(map(int,input().split()))
que = deque(sorted(a))

ans = 0
for i in range(n):
  que.popleft()
  que.pop()
  ans+=que.pop()
  
print(ans)