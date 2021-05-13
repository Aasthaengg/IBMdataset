n = int(input())
s = [input() for _ in range(3)]
ans = 2*n
for i in range(n):
  if s[0][i] == s[1][i]: ans -= 1
  if s[0][i] == s[2][i]: ans -= 1
  if s[2][i] == s[1][i]: ans -= 1
  if s[0][i] == s[1][i] and s[2][i] == s[1][i] : ans += 1
print(ans)
