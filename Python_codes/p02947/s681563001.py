from collections import defaultdict
N = int(input())

S = defaultdict(int)

for i in range(N):
  s = sorted(input())
  s = "".join(s)
  S[s] += 1
  
res = 0
for val in S.values():
  res += val * (val-1) // 2

print(res)