A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
asorted = sorted(a)
bsorted = sorted(b)
cost = {asorted[0]+bsorted[0]}

for i in range(M):
  x, y, c = map(int, input().split())
  cost.add(a[x-1]+b[y-1]-c)
cost = sorted(cost)
print(cost[0])