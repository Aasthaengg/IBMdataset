s = input()

l = 0
r = len(s)-1

rlt = 0

while l<=r:
  if s[l] == 'x':
    if s[r] != 'x':
      rlt += 1
      l += 1
    else:
      l += 1
      r -= 1
  elif s[r] == 'x':
    rlt += 1
    r -= 1
  else:
    if s[l] != s[r]:
      print(-1)
      exit()
    else:
      l += 1
      r -= 1
      
print(rlt)