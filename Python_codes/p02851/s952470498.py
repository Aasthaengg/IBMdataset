def solve():
  from itertools import accumulate
  from sys import stdin
  
  f_i = stdin
  N, K = map(int, f_i.readline().split())
  A = map(int, f_i.readline().split())
  S = accumulate(a - 1 for a in A)
  S = (0, ) + tuple(s % K for s in S)
  
  rec = {}
  ans = 0
  for j, S_j in enumerate(S):
    if j >= K:
      rec[S[j-K]] -= 1
    if S_j in rec:
      ans += rec[S_j]
      rec[S_j] += 1
    else:
      rec[S_j] =1
  
  print(ans)

solve()