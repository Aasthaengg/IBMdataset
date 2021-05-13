def solve():
  X = int(input())
  ans = 0
  cnt = 0
  while cnt<X:
    ans += 1
    cnt += ans
  return ans
print(solve())