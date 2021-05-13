N = int(input())
K = int(input())
ans = float('inf')
for i in range(2**N):
  a = 1
  for j in range(N):
    if (i>>j)&1:
      a *= 2
    else:
      a += K
  ans = min(ans, a)
print(ans)