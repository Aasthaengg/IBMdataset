n, a, b = map(int, input().split())
ans = 0
for num in range(n + 1):
  sum_digit = sum([int(digit) for digit in str(num)])
  if sum_digit >= a and sum_digit <= b:
    ans += num
print(ans)
