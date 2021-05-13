n = int(input())
SP = [list(input().split()) for _ in range(n)]

SPN = [[s, int(p), i + 1] for i, (s, p) in enumerate(SP)]
SPN.sort(key=lambda x: (x[0], -x[1]))

for _, _, i in SPN:
  print(i)