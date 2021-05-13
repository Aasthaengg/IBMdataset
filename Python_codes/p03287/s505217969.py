from collections import Counter
from itertools import accumulate 
import sys
input = sys.stdin.readline
def solve():
  n,m = (int(i) for i in input().split())
  a = list(int(i) for i in input().split())
  a2 = [0] + list(accumulate(a))

  for i in range(n+1):
    a2[i] %= m
  c = Counter(a2)
  ans = 0
  for i in c.values():
    ans += i*(i-1)//2
  print(ans)
if __name__ == "__main__":
  solve()