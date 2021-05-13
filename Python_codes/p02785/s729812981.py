N, K = list(map(lambda n: int(n), input().split(" ")))
HP = list(map(lambda hp: int(hp), input().split(" ")))
HP.sort(reverse=True)

if K >= len(HP):
  print(0)
else:
  print(sum(HP[K:]))