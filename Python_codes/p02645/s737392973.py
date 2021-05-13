s = input()
ans = ''
cnt = 0
for c in s:
  if c.islower():
    ans += c
    cnt += 1
  else:
    ans = ''
    cnt = 0
  if cnt == 3:
    break
    
print(ans)