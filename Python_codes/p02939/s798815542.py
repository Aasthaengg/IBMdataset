s = input()
res = 1
i = 1
while i < len(s)-2:
  if s[i] == s[i-1]:
    i += 3
    res += 2
  else:
    res += 1
    i += 1
if i == len(s):
  print(res)
elif i == len(s)-1:
  if s[-1] == s[-2]:
    print(res)
  else:
    print(res+1)
elif i == len(s)-2:
  if s[-1] == s[-2]:
    print(res+1)
  else:
    if s[-1]==s[-2] or s[-2] == s[-3]:
      print(res+1)
    else:
      print(res+2)