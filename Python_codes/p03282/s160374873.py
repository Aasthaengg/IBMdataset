s = input()
k = int(input())
l = 0
ans = 0
for i in range(len(s)):
  if s[i] == '1':
    l += 1
    if k == l:
      ans = 1
      break
  else:
    ans = int(s[i])
    break
print(ans)