n, p = map(int, input().split())
even_count = sum(a % 2 == 0 for a in map(int, input().split()))
odd_count = n - even_count
if odd_count == 0:
  print(0 if p == 1 else 2 ** even_count)
else:
  print((2 ** even_count) * (2 ** (odd_count - 1)))