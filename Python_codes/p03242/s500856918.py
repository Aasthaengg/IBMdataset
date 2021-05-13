S = input()
N = len(S)
ans = ''
for n in range(N):
  if S[n] == '1':
    ans += '9'
  elif S[n] == '9':
    ans += '1'
  else:
    ans += S[n]
print(ans)