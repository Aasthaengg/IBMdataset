N, x = map(int, input().split())
A = list(map(int, input().split()))
pre_a = 0
ans = 0
for a in A:
  if a > x - pre_a:
    ans += a - (x - pre_a)
    pre_a = x - pre_a
  else:
    pre_a = a

print(ans)