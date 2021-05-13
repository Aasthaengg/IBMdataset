N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for i in range(K+1):
  for j in range(N, max(N-1-(K-i), i-1), -1):
    bag = []
    bag += V[:i] + V[j:]
    bag.sort()
    idx = 0
    if len(bag) == 0:
      continue
    if len(bag) == 1:
      ans = max(ans, sum(bag))
      continue
    if len(bag) == K:
      ans = max(ans, sum(bag))
      continue
    tmp = 0
    for k in range(min(K-len(bag), len(bag))):
      if bag[k] < 0:
        tmp -= bag[k]
    ans = max(ans, sum(bag)+tmp)
print(ans)
