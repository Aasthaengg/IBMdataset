k =int(input())
s =input()
ans = ''
if k>len(s):
  k = len(s)
for i in range (k):
  ans = ans+s[i]

if k<len(s):
  print(ans+'...')
else:
  print(ans)