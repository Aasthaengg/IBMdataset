n = input()
a = len(n)  # 桁数
if a % 2 == 0:  # 桁数が偶数
  ans = "90" * (a // 2)
  ans = int(ans[:-1])
else:
  if a == 1:
    ans = int(n)
  else:
    ans = "90" * ((a - 1) // 2)
    ans = int(ans[:-1])
    ans += int(n) - 10 ** (a - 1) + 1
print(ans)