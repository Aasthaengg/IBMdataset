S = input()
ans = 0
tmpl = 0
tmpr = 0
for i in range(len(S) - 1):
  if S[i] == '<':
    tmpl += 1
  else:
    tmpr += 1
    if S[i + 1] == '<':
      x = max(tmpl, tmpr)
      y = min(tmpl, tmpr)
      ans += (1 + x) * x // 2 + y * (y - 1) // 2
      tmpl = 0
      tmpr = 0

if S[-1] == '<':
  tmpl += 1
else:
  tmpr += 1
x = max(tmpl, tmpr)
y = min(tmpl, tmpr)
ans += (1 + x) * x // 2 + y * (y - 1) // 2
print(ans)