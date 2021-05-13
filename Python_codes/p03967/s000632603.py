import sys
input = sys.stdin.readline
S = list(input())[: -1]
g = 0
p = 0
res = 0
for i in range(len(S)):
  if g > p:
    p += 1
    res += S[i] == "g"
  else:
    g += 1
    res -= S[i] == "p"
print(res)