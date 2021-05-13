import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())

AB = [list(map(int,readline().split())) for i in range(N)]

AB = sorted(AB, key = lambda x:x[0])
amount = 0
for a,b in AB:
  amount += b
  if amount >= K:
    print(a)
    break
