K, A, B = map(int, input().split())
if B - A > 2:
  ans = max(B + ((K - (A + 1)) // 2) * (B - A) + (K - (A + 1)) % 2, K + 1)
else:
  ans = K + 1
  
print(ans)