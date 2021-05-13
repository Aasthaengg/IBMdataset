def calc_log2_int(n):
  """
  calc maximum integer m, such that 2 ^ m <= n 
  """
  left = -1
  right = 100    # 2^100 = 10^30
  while right - left > 1:
    mid = (right + left) // 2
    if pow(2, mid) > n:
      right = mid
    else:
      left = mid
  return left


x, y = map(int, input().split())
n = y // x
print(calc_log2_int(n) + 1)
