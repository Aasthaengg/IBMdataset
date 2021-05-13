S = input()

A = 'gp' * (len(S)//2)
if len(S) % 2 == 1:
  A += 'g'
ans = 0
for i in range(len(S)):
  if S[i] == 'p' and A[i] == 'g':
    ans -= 1
  elif S[i] == 'g' and A[i] == 'p':
    ans += 1
print(ans)