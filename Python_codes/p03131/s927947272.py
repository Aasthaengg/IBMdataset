K, A, B = map(int, input().split())
ans = 0
if B - A <= 2:
  print(K + 1)

else:
  K -= A - 1
  ans += (K//2) * (B - A) + A
  ans += K % 2
  print(ans)
    
