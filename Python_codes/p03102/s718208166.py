n, m, c = map(int, input().split())
lis_b = list(map(int, input().split()))
ans = 0
for _ in range(n):
  goukei = 0
  lis_a = list(map(int, input().split()))
  for a, b in zip(lis_a, lis_b):
    goukei += a * b
  goukei += c
  if goukei > 0:
    ans += 1
    
print(ans)