def solve():
  S, T = input().split()
  ans = list(map(int, input().split()))
  U = input()
  if U==S:
    ans[0] -= 1
  else:
    ans[1] -= 1
  return ans
print(*solve())