N, K = map(int, input().split())
costs = list(map(int, input().split()))
foods = list(map(int, input().split()))
foods.sort()
costs.sort(reverse=True)

def can_eat(x):
  count = 0
  for i in range(N):
    count += max(0, costs[i]-x//foods[i])
  return count <= K

l, r = -1, 10**12+1
while r-l > 1:
  mid = (l+r)//2
  if can_eat(mid):
    r = mid
  else:
    l = mid
print(r)