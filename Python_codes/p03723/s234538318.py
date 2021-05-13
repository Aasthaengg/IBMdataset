A,B,C = map(int, input().split())
ctr = 0
if A == B == C and A%2 == 0 and B%2 == 0 and C%2 == 0:
  print(-1)
else:
  while A%2 == 0 and B%2 == 0 and C%2 == 0:
    A,B,C = int((B+C)/2), int((A+C)/2), int((A+B)/2)
    ctr += 1
  print(ctr)