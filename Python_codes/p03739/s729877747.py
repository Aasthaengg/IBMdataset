n = int(input())
A = list(map(int, input().split()))
def solve(A, p):
  act = 0
  total = 0
  for a in A:
    total += a
    if total * p < 1:
      act += abs(p - total)
      total = p
    p *= -1
  return act
ans = min(solve(A, 1), solve(A, -1))
print(ans)