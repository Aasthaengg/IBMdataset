s = input()
ans = len(s) // 2
for i in s:
  if i == 'p':
    ans -= 1
print(ans)