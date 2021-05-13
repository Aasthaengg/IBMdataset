import sys
input = sys.stdin.readline
import bisect

a, b, q = map(int, input().split())
S = [int(input()) for _ in range(a)]
T = [int(input()) for _ in range(b)]

for _ in range(q):
  x = int(input())
  s_bi = bisect.bisect_right(S, x)
  t_bi = bisect.bisect_right(T, x)
  s_left = S[s_bi-1] if s_bi>0 else -float("inf")
  s_right = S[s_bi] if s_bi<a else float("inf")
  t_left = T[t_bi-1] if t_bi>0 else -float("inf")
  t_right = T[t_bi] if t_bi<b else float("inf")
  c = x - min(s_left, t_left)
  d = max(s_right, t_right) - x
  e = t_right - s_left + min(x-s_left, t_right-x)
  f = s_right - t_left + min(x-t_left, s_right-x)
  ans = min(c, d, e, f)
  print(ans)