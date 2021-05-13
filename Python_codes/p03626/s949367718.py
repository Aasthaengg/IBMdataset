N = int(input())
S0 = input()
S1 = input()

tate = []
ikkome = True
S = ''
for i in range(N):
  if S0[i] == S1[i]:
    tate.append(i)
    S = S + 'T'
  else:
    if ikkome:
      S = S + 'Y'
      ikkome = False
    else:
      ikkome = True

now = S[0]
if now == 'T':
  ans = 3
else:
  ans = 6
  
if len(S) == 1:
  print(ans)
  exit()
  
S = S[1:]
MOD = 1000000007
for si in S:
  if now == 'T':
    if si == 'T':
      ans = ans * 2 % MOD
    else:
      ans = ans * 2 % MOD
      now = 'Y'
  else:
    if si == 'Y':
      ans = ans * 3 % MOD
    else:
      now = 'T'
print(ans)

