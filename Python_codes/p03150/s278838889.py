s = input()
ans = ''
if s == 'keyence':
  ans = 'YES'
else:
  for i in range(len(s) - 7):
    for j in range(len(s) - i):
      if s[:j] + s[j + i + 1:] == 'keyence':
        ans = 'YES'
        break
if ans == '':
  ans = 'NO'
print(ans)