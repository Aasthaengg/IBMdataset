def solve():
  N = int(input())  
  K = int(input())
  ans = 1
  for _ in range(N):
    if ans<K:
      ans *= 2
    else:
      ans += K
  return ans
print(solve())