n, *S = open(0)
n = int(n)
a = b = ba = c = 0
for i in range(n):
  S[i] = S[i].strip()
  if S[i][-1]=='A' and S[i][0]=='B':
    ba += 1
  else:
    a += S[i][-1]=='A'
    b += S[i][0]=='B'
  c += S[i].count('AB')
if ba == 0:
  print(c + min(a, b))
elif a+b == 0:
  print(c + ba-1)
else:
  print(c + ba + min(a, b))