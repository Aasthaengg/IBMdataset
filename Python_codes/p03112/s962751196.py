import bisect
import itertools

A,B,Q = map(int,input().split())

INF = float('inf')
S = [-INF] + [int(input()) for _ in range(A)] + [INF]
T = [-INF] + [int(input()) for _ in range(B)] + [INF]
X = [int(input()) for _ in range(Q)]

def solve(x):
  i = bisect.bisect_left(S, x)
  j = bisect.bisect_left(T, x)
  result = INF
  # どの2つを目指すか
  for s,t in itertools.product(S[i-1:i+1], T[j-1:j+1]):
    d = min(abs(s-x),abs(t-x)) + abs(t-s) # tがsとxの間に入るか否か
    result = min(result,d)
  return result

for x in X:
  ans = solve(x)
  print(ans)
