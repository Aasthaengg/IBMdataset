n, m = [int(i) for i in input().split()]
td = [[int(i) for i in input().split()] for n in range(n)]
td.sort(key=lambda x:-x[1])
memo = set()
a = []
for t, d in td:
  if t in memo:
    a.append((d, 0))
  else:
    a.append((d, 1))
  memo.add(t)
a = [(-x, x, d) for x, d in a]
import heapq
heapq.heapify(a)
val = 0
kind = 0
b = []
for _ in range(m):
  ele = heapq.heappop(a)
  val += ele[1]
  kind += ele[2]
  if ele[2] == 0:
    b.append(ele[1])
ans = val + kind ** 2
while (len(a) > 0 and len(b)>0):
  val -= b.pop()
  flag = False
  while(len(a) > 0):
    elem = heapq.heappop(a)
    if elem[2] == 1:
      flag = True
      break
  if not flag:
    break
  val += elem[1]
  kind += 1
  tmpans = val + kind ** 2
  if tmpans > ans:
    ans = tmpans
print(ans)