# すべての頂点が入力に現れる回数が偶数であればOK 奇数回の頂点が一つでもあればNO
from collections import defaultdict as d

N,M = map(int,input().split())
E = d(int)

for i in range(M):
  a,b = map(int,input().split())
  E[a] ^= 1
  E[b] ^= 1

print(("YES","NO")[sorted(E.values())[-1]])
