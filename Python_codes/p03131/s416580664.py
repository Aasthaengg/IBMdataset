K, A, B = map(int, input().split())

if B-A <= 2:
  ans = K+1
else:
  ans = A
  n = (K-A+1) // 2
  ans += (B-A) * n
  if (K-A+1) % 2 == 1:
    ans += 1
print(ans)