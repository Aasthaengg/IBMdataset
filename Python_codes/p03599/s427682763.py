import sys
input = sys.stdin.readline

A,B,C,D,E,F = list(map(int, input().split()))

W = set()
for a in range(0, F+1, A*100):
  for b in range(0, F+1, B*100):
    w = a+b
    if w==0 or w>F: continue
    W.add(w)

S = set()
for c in range(0, F+1, C):
  for d in range(0, F+1, D):
    s = c+d
    if s>F: continue
    S.add(s)

d_max = -1
ans = None
for w in W:
  for s in S:
    if w*E//100<s or w+s>F: continue
    d = 100*s/(w+s)
    if d>d_max:
      d_max = d
      ans = (w+s, s)

print(*ans)