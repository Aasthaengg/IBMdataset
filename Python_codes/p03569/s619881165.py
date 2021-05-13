s = input()
cnt = 0

while True:
  if len(s) < 2:
    break
  if s[0] == s[-1]:
    s = s[1:-1]
  elif s[0] == 'x':
    s += 'x'
    cnt += 1
  elif s[-1] == 'x':
    s = 'x' + s
    cnt += 1
  else:
    print (-1)
    exit()
print (cnt)
