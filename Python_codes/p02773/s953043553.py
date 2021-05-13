from collections import Counter
def solve():
  N = int(input())
  S = [input() for _ in range(N)]
  c = Counter(S)
  M = max(c.values())
  ans = []
  for k,v in c.items():
    if v==M:
      ans.append(k)
  ans.sort()
  return ans
print(*solve(),sep='\n')