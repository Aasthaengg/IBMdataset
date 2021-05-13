n = int(input())
ans = 10 ** 9
for a in range(1, n):
  b = n - a
  total = sum([int(digit_a) for digit_a in str(a)]) + sum([int(digit_b) for digit_b in str(b)])
  if total < ans:
    ans = total
print(ans)
