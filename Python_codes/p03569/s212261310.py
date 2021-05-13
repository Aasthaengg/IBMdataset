s = input()
if len(s) == 1:
  print(0)
else:
  left = 0
  right = len(s)-1
  ans = 0
  while left <= right:
    if s[left] == s[right]:
      left += 1
      right -= 1
    elif s[left] == 'x':
      ans += 1
      left += 1
    elif s[right] == 'x':
      ans += 1
      right -= 1
    else:
      ans = -1
      break
  print(ans)