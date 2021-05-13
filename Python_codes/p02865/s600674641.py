
import sys
input = sys.stdin.readline
def solve():
  n = int(input())
  ans = 0
  for i in range(1,1+n//2):
    j = n-i
    if j > i:
      ans += 1
  print(ans)
solve()