N = int(input())
S = [input() for _ in range(N)]
S_set = set(S)
M = int(input())
T = [input() for _ in range(M)]
m = 0
for s in S_set:
  m = max(m, S.count(s)-T.count(s))
print(m)