s = str(input())
check = s.replace('x', '')

if check == check[::-1]:
  left = 0
  right = len(s)-1
  ans = 0
  while left < right:
    if s[left] == s[right]:
      left += 1
      right -= 1
    else:
      if s[left] == 'x':
        s = s[:right+1] + 'x' + s[right+1:]
      else:
        s = s[:left] + 'x' + s[left:]
      left += 1
      ans += 1
  print(ans)
else:
  print(-1)