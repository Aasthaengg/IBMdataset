from collections import deque
N = int(input())
a = list(map(int,input().split()))
pow = 0
a = deque(sorted(a,reverse = True))
for i in range(N):
  a.popleft()
  pow += a.popleft()
  a.pop()
print(pow)