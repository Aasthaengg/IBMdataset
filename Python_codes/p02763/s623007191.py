n = int(input())
S = list(input())
q = int(input())

import sys
input = sys.stdin.readline

alp = "abcdefghijklmnopqrstuvwxyz"
appr = {a:[] for a in alp}

import bisect

for i, a in enumerate(S):
  appr[a].append(i+1)
#print(appr)
for i in range(q):
  inputs = input().split()
  if inputs[0] == '1':
    c = int(inputs[1])
    a = inputs[2]
    if S[c-1]==a:
      continue
    else:
      old = S[c-1]
      S[c-1] = a
      del_idx = bisect.bisect_left(appr[old], c)
      del appr[old][del_idx]
      in_idx = bisect.bisect_left(appr[a], c)
      appr[a].insert(in_idx, c)
  else:
    l, r = map(int, inputs[1:])
    res = 0
    for a in appr:
      l_idx = bisect.bisect_left(appr[a], l)
      if l_idx<len(appr[a]):
        if appr[a][l_idx]<=r:
          res += 1
    print(res)
    
#print(appr)