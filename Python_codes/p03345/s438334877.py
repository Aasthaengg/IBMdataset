A,B,C,K = map(int,input().split())
S = A + B + C
S += S * K

if K % 2 == 0:
  # 差がそのまま
  S -= (B-A) + (C-A)
  a = S // 3
  b = a + (B-A)
  ans = a - b
else:
  # 差が逆
  S -= (A-B) + (A-C)
  a = S // 3
  b = a + (A-B)
  ans = a - b
  
if abs(ans) > 10 ** 18:
  print("Unfair")
  exit()
  
print(ans)


