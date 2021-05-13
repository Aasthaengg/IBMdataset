from collections import defaultdict
from itertools import combinations

N=int(input())
S=[input() for _ in range(N)]

c = defaultdict(int)

for i in range(N):
  if S[i][0] in {'M','A','R','C','H'}:
    c[S[i][0]] += 1

if len(c) < 3:
  print(0)
  exit()

if len(c)==3:
  ans=1
  for k in c.keys():
    ans *= c[k]
  print(ans)
  exit()

else:
  ans = 0
  l = len(c)
  keys = list(c.keys())
  for C in combinations(range(l),3):
    tmp = c[keys[C[0]]]*c[keys[C[1]]]*c[keys[C[2]]]
    ans += tmp
  print(ans)