S = list(input())
if(S[-1]=='s'):
  ans = ''
  for i in range(len(S)):
    ans += S[i]
  ans += 'e'
  ans += 's'
  print(ans)
else:
  ans = ''
  for i in range(len(S)):
    ans += S[i]
  ans += 's'
  print(ans)