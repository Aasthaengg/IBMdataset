s = list(input())
n = len(s)
ans = "yes"
for i in range(n):
  if s.count(s[i]) != 1:
    ans = "no"
print(ans)