from collections import Counter
import heapq
N,M = map(int,input().split())
A = Counter(list(map(int,input().split())))

cards = []
for x,y in A.items():
  heapq.heappush(cards, (-x,y))

for _ in range(M):
  b,c = map(int,input().split())
  heapq.heappush(cards, (-c,b))
cnt = N
ans = 0
while cnt <= N:
  v,c = heapq.heappop(cards)
  v *= -1
  if cnt-c < 0:
    ans += v*cnt
    break
  else:
    ans += v*c
    cnt -= c

print(ans)
