n = int(input())
sum_abs_a = 0
min_abs_a = 10 ** 9
minus_odd = False
for a in map(int, input().split()):
  if a < 0:
    minus_odd = not minus_odd
    a = -a
  sum_abs_a += a
  min_abs_a = min(min_abs_a, a)
if minus_odd:
  print(sum_abs_a - 2 * min_abs_a)
else:
  print(sum_abs_a)