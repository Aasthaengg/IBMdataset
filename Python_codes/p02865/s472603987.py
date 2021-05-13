n = int(input())

ans = 0
if n % 2 == 0:
  # 偶数
  ans = (n / 2) - 1
else:
  ans = n // 2

print(int(ans))