K, A, B = map(int, input().split())
if B - A <= 2 :
  print(K + 1)
elif K < A + 1:
  print(K + 1)
elif K == A + 1:
  print(B)
else:
  count = K - (A + 1)
  if count % 2 == 0:
    ans = count // 2 * (B - A) + B
  else:
    ans = count//2 * (B - A) + B + 1
  print(ans)