N = int(input())
S1 = input()
S2 = input()
MOD = 10 ** 9 + 7
if S1[0] == S2[0]:
  ans = 3
  i = 1
  f = True
else:
  ans = 6
  i = 2
  f = False

while i < N:
  if S1[i] == S2[i]:
    if f:
      ans = ans * 2 % MOD
    f = True
    i += 1
  else:
    if f:
      ans = ans * 2 % MOD
    else:
      ans = ans * 3 % MOD
    f = False
    i += 2

print(ans)