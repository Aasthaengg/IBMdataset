import heapq

N,M = map(int,input().split())

T = list(map(int,input().split()))

memo = []
for t in T:
    memo.append(-t)
memo.sort()

for m in range(M):
    tmp = heapq.heappop(memo)
    tmp = int(tmp/2)
    heapq.heappush(memo,tmp)
print(-1*sum(memo))
