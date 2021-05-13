n = int(input())
s = input()
if len(s)>1:
  n = len(s)//2
  if s[0:n]==s[n:]:
    print('Yes')
  else:
    print('No')
else:
  print('No')