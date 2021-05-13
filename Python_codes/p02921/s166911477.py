s = input()
t = input()

ans = 0
for i,data in enumerate(s):
  if s[i] == t[i]:
    ans += 1

print(ans)