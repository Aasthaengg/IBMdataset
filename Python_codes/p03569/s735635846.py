s = input()
flag = True
top = 0
tale = len(s)-1
ans = 0
while top < tale:
  if s[top] == 'x' and s[tale] == 'x':
    top += 1
    tale -= 1
  elif s[top] == 'x' and s[tale] != 'x':
    top += 1
  elif s[top] != 'x' and s[tale] == 'x':
    tale -= 1
  else:
    if s[top] != s[tale]:
      flag = False
      break
    else:
      top += 1
      tale -= 1
if not flag:
  print(-1)
else:
  top = 0
  tale = len(s)-1
  while top < tale:
    if s[top] == s[tale]:
      top += 1
      tale -= 1
    elif s[top] == 'x' and s[tale] != 'x':
      ans += 1
      top += 1
    elif s[top] != 'x' and s[tale] == 'x':
      ans += 1
      tale -= 1
  print(ans)