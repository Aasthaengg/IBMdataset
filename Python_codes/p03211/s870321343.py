s = input()

ans = float("inf")
for i in range(len(s)-2):
  t = abs(753 - int(s[i:i+3]))
  if t < ans: ans = t
print(ans)