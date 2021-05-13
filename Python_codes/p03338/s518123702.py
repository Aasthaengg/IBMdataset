n = int(input())
s = input()

ans = 0
for i in range(1,n):
  t = len(set(s[:i]) & set(s[i:]))
  if ans < t: ans = t
print(ans)