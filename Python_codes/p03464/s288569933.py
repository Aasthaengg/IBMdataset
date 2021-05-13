def solve():
  ans = 0
  K = int(input())
  A = list(map(int, input().split()))
  A = A[::-1]
  bottom = 2
  top = 2
  for a in A:
    bottom = -(-bottom//a)*a
    if bottom>top:
      return [-1]
    top = top//a*a+a-1
  return [bottom,top]
print(*solve())