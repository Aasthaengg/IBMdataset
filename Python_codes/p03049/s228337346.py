N = int(input())
ans = 0
a, b, ab = 0, 0, 0
for _ in range(N):
  s = input()
  ans += s.count('AB')
  if s[-1] == 'A' and s[0] == 'B':
    ab += 1
  elif s[-1] == 'A':
    a += 1
  elif s[0] == 'B':
    b += 1
if ab > 0:
  ans += ab-1
  if a > 0:
    ans += 1
    a -= 1
  if b > 0:
    ans += 1
    b -= 1
ans += min(a, b)
print(ans)