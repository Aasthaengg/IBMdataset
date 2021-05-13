import sys
input = sys.stdin.readline

N,M=(int(x) for x in input().rstrip('\n').split())
As = [int(x) for x in input().rstrip('\n').split()]
d = {}
for x in As:
  if x in d:
    d[x] += 1
  else:
    d[x] = 1
for _ in range(M):
  B,C = (int(x) for x in input().rstrip('\n').split())
  if C in d:
    d[C] += B
  else:
    d[C] = B
res = 0
rest = N
d2 = sorted([x for x in d.keys()],reverse=True)
for m in d2:
  x = d[m]
  if rest < x:
    res += rest*m
    break
  else:
    res += x*m
    rest -= x
print(res)