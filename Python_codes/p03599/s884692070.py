a, b, c, d, e, f = map(int, input().split())
w = []
s = []
for i in range(f // (100 * a) + 1):
  for j in range((f - 100 * a * i) // (100 * b) + 1):
    if 100 * a * i + 100 * b * j <= f:
      w.append(100 * a * i + 100 * b * j)
for i in range(f // c + 1):
  for j in range((f - c * i) // d + 1):
    if c * i + d * j <= f:
      s.append(c * i + d * j)
w.sort()
s.sort()
ans = (100 * a, 0)
l = 0
for i in w:
  for j in range(l, len(s)):
    if i + s[j] > f:
      break
    if s[j] > i // 100 * e:
      break
    l = j
    if ans[1] * i < s[j] * ans[0]:
      ans = (i, s[j])
print(ans[0] + ans[1], ans[1])
