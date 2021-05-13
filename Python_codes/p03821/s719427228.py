from collections import deque
N = int(input())
d = deque([])
for i in range(N):
  a, b = map(int, input().split())
  d.appendleft([a, b])

cnt = 0
ans = 0
for n in d:
  if (n[0]+cnt) % n[1] != 0:
    ans += n[1] - ((n[0]+cnt)%n[1])
    cnt += n[1] - ((n[0]+cnt)%n[1])
print(ans)