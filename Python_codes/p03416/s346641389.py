a, b = map(int, input().split())
cnt = 0
for k in range(a, b+1):
  k = str(k)
  t = ''
  for i in range(1, len(k) + 1):
    t += k[-i]
  if k == t:
    cnt += 1
print(cnt)