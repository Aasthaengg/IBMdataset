def solve():
  A = [int(input()) for _ in range(5)]
  m = 0
  ans = 0
  for a in A:
    ans += -(-a//10)*10
    if a%10>0:
      m = max(m,10-a%10)
  ans -= m
  return ans
print(solve())