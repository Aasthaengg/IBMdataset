s = list(map(str,input().split()))
ans = 0
if s[1]=='+':
  ans = int(s[0])+int(s[2])
else:
  ans = int(s[0])-int(s[2])
print(ans)
