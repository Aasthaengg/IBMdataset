s = input()

for w in s:
  cnt = s.count(w)
  if cnt > 1:
    ans = 'no'
    break
  else:
    ans = 'yes'
    
print(ans)