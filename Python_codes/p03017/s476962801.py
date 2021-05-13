n, a, b, c, d = map(int, input().split())
s = input()

if a > b and c > d or a < b and c < d:
  if s[a - 1:c].count('##') + s[b - 1:d].count('##') == 0:
    print('Yes')
  else:
    print('No')
else:
  i, j = (b, d) if a < b else (a, c)
  if any(s[k - 1] == s[k] == s[k + 1] == '.' for k in range(i - 1, j)):
    print('Yes')
  else:
    print('No')