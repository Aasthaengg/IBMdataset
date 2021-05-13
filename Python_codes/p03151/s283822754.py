n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from bisect import bisect_left

def solve(n, A, B):
  if sum(A) < sum(B):
    print(-1)
    return

  under = []
  over = []
  for a, b in zip(A, B):
    if a < b: under.append(b-a)
    elif a > b: over.append(a-b)

  over_acc = [0]
  for v in sorted(over, reverse=True):
    over_acc.append(over_acc[-1] + v)

  ans = len(under)
  ans += bisect_left(over_acc, sum(under))
  print(ans)

solve(n, A, B)