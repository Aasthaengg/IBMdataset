s = input()

ans = 1000

for i in range(len(s)-2):
  t = int(s[i:i+3])
  a = abs(753 - t)
  ans = min(ans, a)

print(ans)