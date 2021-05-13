N = int(input())

ans = float('inf')
a, b = 1, N-1
while a <= b:
  sum_d_a = sum(map(int, str(a)))
  sum_d_b = sum(map(int, str(b)))
  ans = min(ans, sum_d_a + sum_d_b)
  a += 1
  b -= 1

print(ans)