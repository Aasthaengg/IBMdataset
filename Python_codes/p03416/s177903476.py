a, b = map(int, input().split())
ans = 0
for num in range(a, b + 1):
  str_num = str(num)
  i = len(str_num) // 2
  if str_num[:i] == str_num[:i:-1]:
    ans += 1
print(ans)