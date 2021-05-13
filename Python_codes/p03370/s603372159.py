n, x = map(int, input().split())
ans = n
sum_dounut = 0
min_val = 10 ** 9
for _ in range(n):
  m = int(input())
  sum_dounut += m
  if m < min_val:
    min_val = m
print(ans + ((x - sum_dounut) // min_val))
