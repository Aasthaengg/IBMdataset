S = input()
n = len(S)
ans = 'NO'
for i in range(n):
  j = i+n-7
  Q = S[:i] + S[j:]
  if Q == 'keyence':
    ans = 'YES'
print(ans)