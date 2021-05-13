N, K = map(int, input().split())
monsters = list(map(int, input().split()))
monsters.sort()
if N <= K:
  print(0)
else:
  print(sum(monsters[:N-K]))