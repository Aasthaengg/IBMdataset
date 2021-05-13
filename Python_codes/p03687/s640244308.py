S = input()
rests = [chr(i) for i in range(97, 97+26)]

def is_only(s, c):
  for sc in s:
    if sc != c:
      return False
  return True

def shrink(s, c):
  res = ''
  for i in range(len(s)-1):
    if s[i+1] == c:
      res += c
    else:
      res += s[i]
  return res

ans = 10**3
for c in rests:
  if not c in S:
    continue
  s = S
  cnt = 0
  while not is_only(s, c):
    s = shrink(s, c)
    cnt += 1
  ans = min(ans, cnt)
print(ans)