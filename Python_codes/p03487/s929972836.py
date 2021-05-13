from collections import Counter
def solve():
  ans = 0
  N = int(input())
  A = list(map(int, input().split()))
  c = Counter(A)
  for k,v in c.items():
    if k<=v:
      ans += v-k
    else:
      ans += v
  return ans
print(solve())