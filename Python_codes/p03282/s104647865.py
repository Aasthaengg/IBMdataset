import sys
S = input()
K = int(input())

k=0
for s in S:
  s = int(s)
  k += 1
  if not s == 1:
    print(s)
    sys.exit()
  elif k == K:
    print(1)
    sys.exit()