s = input()
i = res = 0
tmp = ''
while i < len(s):
  if tmp == s[i]:
    if i == len(s) - 1:
      break
    else:
      tmp = s[i] + s[i+1]
      i += 2
  else:
    tmp = s[i]
    i += 1
  res += 1
print(res)