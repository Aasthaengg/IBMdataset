S = input()
n = len(S)
ans = 0
for bit in range(2**(n-1)):
  x = S[0]
  for i in range(n-1):
    if bit & (1<<i):
      x += '+'
    x += S[i+1]
  ans += sum(map(int, x.split('+')))
print(ans)