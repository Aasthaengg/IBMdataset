import sys
input = sys.stdin.readline
S = list(input())[: -1]
res = 0
for l in range(len(S)):
  for r in range(l + 1, len(S) + 1):
    for i in range(l, r):
      if not S[i] in ["A", "T", "C", "G"]: break
    else: res = max(res, r - l)
print(res)