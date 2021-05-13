def greatest_common_divisor(a, b):
  if a == 0 or b == 0:
    return max(a, b)

  return greatest_common_divisor(max(a, b) - min(a, b), min(a, b))

a, b = map(int, input().split())
print(greatest_common_divisor(a, b))