s = input()
n = len(s)
ans = ""
for i in range(n):
  if s[i] == "?":
    ans += "D"
  else:
    ans += s[i]
print(ans)
