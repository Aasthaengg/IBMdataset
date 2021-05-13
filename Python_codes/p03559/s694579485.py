from bisect import bisect

N = int(input())
aa = sorted(list(map(int,input().split())))
bb = sorted(list(map(int,input().split())))
cc = sorted(list(map(int,input().split())))

b_cost = [0]

for i,b in enumerate(bb):
  b_cost.append(N-bisect(cc, b)+b_cost[i])

ans = 0
for a in aa:
  idx = bisect(bb, a)
  ans += b_cost[-1]-b_cost[idx]
print(ans)