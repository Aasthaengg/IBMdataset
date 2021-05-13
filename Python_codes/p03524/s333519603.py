S = list(input())
N = len(S)
a = 0
b = 0
c = 0
for i in range(N):
  if S[i] == 'a':
    a += 1
  elif S[i] == 'b':
    b += 1
  else:
    c += 1
if N == 1:
  ans = 'YES'
elif N == 2:
  if max(a, b, c) == 2:
    ans = 'NO'
  else:
    ans = 'YES'
else:
  if min(a, b, c) == 0:
    ans = 'NO'
  elif max(a, b, c) - min(a, b, c) < 2:
    ans = 'YES'
  else:
    ans = 'NO'
print(ans)