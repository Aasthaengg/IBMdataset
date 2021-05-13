s = input()
ans = ''
while True:
  i = len(s)//2
  if s[0:i]==s[i:-1]:
    ans = s[0:i]+s[i:-1]
    break
  s = s[0:-1]
print(len(ans))