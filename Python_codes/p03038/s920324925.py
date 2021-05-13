import collections
import heapq

n,m = map(int,input().split())
a = list(map(int,input().split()))
bc = []
for _ in range(m):
    b,c = map(int,input().split())
    bc.append((b,c))
cnt = collections.Counter(a).most_common()
heapq.heapify(cnt)


for i, set_bc in enumerate(bc):
    now0,now1 = heapq.heappop(cnt)
    b,c = set_bc
    if now0 >= c:
        heapq.heappush(cnt,(now0,now1))
        now1 = 0
        continue
    tmpb = 0
    for j in range(b):
        if now0 < c:
            if now1 >= b:
                now1 -= b
                tmpb += b
                heapq.heappush(cnt,(c,tmpb))
                break
            tmpb += now1
            b -= now1
            now0,now1 = heapq.heappop(cnt)
        else:
            heapq.heappush(cnt,(c,tmpb))
            break
    if now1 != 0:
        heapq.heappush(cnt,(now0,now1))
        now1 = 0
if now1 != 0:
    heapq.heappush(cnt,(now0,now1))
ans = 0

for i in range(len(cnt)):
    val, num = heapq.heappop(cnt)
    ans += val * num
print(ans)
