import heapq
from collections import defaultdict
n, m =map(int, input().split())
a=list(map(int, input().split()))

for i in range(n):
  a[i] *= -1


pri=list(set(a))
heapq.heapify(pri)
dict=defaultdict(int)
for i in a:
  dict[-i] += 1
for i in range(m):
  b, c = map(int, input().split())
  dict[c] += b
  heapq.heappush(pri,-c)
# print (pri)
# print (dict)

ans = 0
cnt = 0
old = 0
while True:
  x = heapq.heappop(pri)
  x *= -1
  if old == x:
    continue
  if cnt+dict[x] > n:
    ans += (n-cnt)*x
    cnt += n-cnt
  else:
    ans += dict[x]*x
    cnt += dict[x]
  if cnt >= n:
    break
  old = x
print (ans)
