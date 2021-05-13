from collections import Counter

N = int(input())
a = [int(input()) for _ in range(N)]

def solve(n,a):
  d = Counter(a)
  if len(d) == 1:
    return a
  d_lst = list(sorted(d.keys()))
  first = d_lst[-1]
  second = d_lst[-2]
  if d[first] != 1:
    return [first]*n
  else: # first は一つだけ
    return [second if a[i] == first else first for i in range(n)]

print(*solve(N,a),sep="\n")
