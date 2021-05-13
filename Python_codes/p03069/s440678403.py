_ = input()
S = input().lstrip('.').rstrip('#')
n = len(S)
A = list(S)

x = 0
y = S.count('.')
ans = min(n-y, y)
for i in range(n):
  if S[i] == '#':
    x += 1
  else:
    y -= 1
  ans = min(ans, x + y)
print(ans)