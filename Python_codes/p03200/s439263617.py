s = input()
l=len(s)
ans = 0
W = 0
for i in range(l):
  if s[i] == "W":
    ans += len(s[W:i])
    W += 1

print(ans)